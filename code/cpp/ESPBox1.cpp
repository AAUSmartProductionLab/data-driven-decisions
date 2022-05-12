#include "Arduino.h"
#include "ArduinoJson.h"
#include "dht.h"
#include <iostream>
#include <string>
#include "ESP8266WiFi.h"
#include "PubSubClient.h"
#include "user_interface.h"

//DHT parameters
#define DHTTYPE DHT11
#define DHTPIN D5
DHT dht(DHTPIN, DHTTYPE);

//Timing parameters
int sampleRate = 4.5*60e3; //sample time of 4min 30sec
int rateAdjust = 30e3; //adjust sample time up by 30sec to make full 5min cycle
uint64_t sleepTime = 12*60*60e6;
int comLimit = 24; //number of poll instances per day
int sampleLimit = 6; //number of samples per JSON-object

//WiFi parameters
WiFiClient espClient; ////MQTT Initialization
PubSubClient client(espClient); ////MQTT Initialization
char ssid[] = "raspi-webgui"; //PolyBotNet
const char* password =  "ChangeMe"; //or ChangeMe
const char* mqtt_server = "10.3.141.1"; //192.168.1.191

//MQTT parameters
String espName = "ESPBox1";
String namePub = espName + "/DHT11";

//*********Functions**********
String pollDHT(){  
  //JSON parameters
  const int capacity = JSON_ARRAY_SIZE(5) + 5*JSON_OBJECT_SIZE(3);
  StaticJsonDocument<capacity> doc;
  String buffer;
  //Iterate sampling
  for (int i=0; i<sampleLimit; i++){
      
    doc[i]["hum"] = dht.readHumidity();
    doc[i]["temp"] = dht.readTemperature();
    //delay between samples
    delay(/*sampleRate+rateAdjust*/ 5000);

  }
  
  //convert JSON doc to char buffer
  serializeJson(doc, buffer);

  return buffer.c_str();
}

void connectNetwork(){
  
  WiFi.begin(ssid, password);
  WiFi.mode(WIFI_STA);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println(WiFi.status());
  }

  Serial.println(WiFi.localIP());
  Serial.println("Connected to the WiFi network");
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("inTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}


//**********Set-Up************
void setup() {
  // put your setup code here, to run once:
  //Initiate Serial
  Serial.begin(9600);
  Serial.flush();
  //Initiate dht
  dht.begin();
  //set MQTT server socket
  client.setServer(mqtt_server, 1883);
 

}

//***********Main*************
void loop() {
 
  for (int i=0; i<comLimit; i++) {
    //run pollDHT and store result in a string object
    String vals = pollDHT();
    //Connect to the network
    connectNetwork();
    //If not connected to WiFi, connect to WiFi
    if (!client.connected()) {
      reconnect();
      delay(500);
    }
    
    client.loop();
    //publish c-str() of pollDHT output to MQTT server
    client.publish(namePub.c_str(),vals.c_str());
    //turn off wifi and wait until next polling 
    WiFi.mode(WIFI_OFF);
  }
  ESP.deepSleep(/*sleepTime*/ 2*60e3);
}