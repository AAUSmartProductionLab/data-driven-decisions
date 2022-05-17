
//Libraries
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include "PubSubClient.h"
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_SSD1306.h>
#include "SPI.h"
#include <ArduinoJson.h>
#include <Wire.h>

// Digital pin for IR 
#define IRPIN D0 // Pin for IR dectector
// Digital pin for lightsensor
#define CS D8 // Assignment of the CS pin

//Network parameters and MQTT server IP
char ssid[] = "iiot_case_4"; //iiot_case_1, iiot_case_2, iiot_case_3, iiot_case_4
const char* password =  "robotlab"; //the code for all the WiFis
const char* mqtt_server = "10.3.141.1"; //IP addr for all the cases

//Variables
byte intensity = 0; //Stores sensor value for the light sensor
int detect = 0; //1 or 0 depending on if something is in the way
int flag = 1; // Flag is used to check if something moved in front of irsensor and left again
int status = 0; //Status for linetracker 0 = object has moved, 1 = object detected, 2 = object is still there, 3 = no object detected
unsigned long currentMillis = 0;
unsigned long startMillis = 0;
unsigned long period = 2000;

//Define the name of the ESP
String espName = "ESPBox2";

//MQTT
WiFiClient espClient;
PubSubClient client(espClient);

//IMU Class instance
Adafruit_MPU6050 mpu;

/********************************************************************** NETWORK FUNCTIONS ***************************************************************************/

// connect to network function
void connectNetwork(){
  delay(10);
  pinMode(13, OUTPUT); 
  Serial.begin(115200);

  WiFi.hostname(espName.c_str());
  WiFi.begin(ssid, password);
  WiFi.mode(WIFI_STA);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println(WiFi.status());
  }

  if (!mpu.begin()) {
    Serial.println("Sensor init failed");
    while (1)
      yield();
  }

  Serial.println(WiFi.localIP());
  Serial.println("Connected to the WiFi network");
}

//Attempt to reconnect to MQTT server if the connection is lost
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

/********************************************************************** SENSOR FUNCTIONS ***************************************************************************/
void imu(){
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  
  String jsonString;
  DynamicJsonDocument doc(1024);

  doc["sensor"] = "IMU";
  doc["timestamp"]   = "time";

  doc["acceleration"][0] = a.acceleration.x;
  doc["acceleration"][1] = a.acceleration.y;
  doc["acceleration"][2] = a.acceleration.z;

  doc["gyroscope"][0] = g.gyro.x;
  doc["gyroscope"][1] = g.gyro.y;
  doc["gyroscope"][2] = g.gyro.z;

  serializeJson(doc, jsonString);
  Serial.println(jsonString);
  String namePub = espName + "/imu";

  client.publish(namePub.c_str(), jsonString.c_str());
}

void lineTracker(){
    detect = digitalRead(IRPIN);
    if (detect == 0 && flag == 0){
      flag = 1;
      status = 0;
      Serial.println("Object has moved on!");
    }
    else if (detect == 1 && flag == 1){
      flag = 0;
      status = 1;
      Serial.println("Object has been detected!");
    }
    else if (detect == 1 && flag == 0){
      status = 2;
     Serial.println("Object is still here!");
    }
    else if (detect == 0 && flag == 1){
      status = 3;
      Serial.println("There is no object!");
    }
    String namePub = espName + "/tracker";

    String jsonString;
    DynamicJsonDocument doc(1024);

    doc["sensor"] = "LineTracker";
    doc["timestamp"] = "time";
    doc["status"] = status;

    serializeJson(doc, jsonString);

    Serial.println(jsonString);

    client.publish(namePub.c_str(), jsonString.c_str());
}

void lightSensor(){
  digitalWrite(CS, LOW); // activation of CS line
  intensity = SPI.transfer(0) << 3; // Aquisition of first 5 bits of data without leading zeros
  intensity |= (SPI.transfer(0) >> 4); //Aquisition of last 3 bits of data and appending
  digitalWrite(CS, HIGH);
  String namePub = espName + "/light";
  
  String jsonString;
  DynamicJsonDocument doc(1024);

  doc["sensor"] = "LightSensor";
  doc["timestamp"] = "time";
  doc["intensity"] = float(intensity);

  serializeJson(doc, jsonString);

  Serial.println(jsonString);

  client.publish(namePub.c_str(), jsonString.c_str());

  delay(200);
}

/********************************************************************** SETUP AND LOOP FUNCTIONS ***************************************************************************/
void setup() {
  connectNetwork();

  SPI.begin(); // initialization of SPI port
  SPI.setDataMode(SPI_MODE0); // configuration of SPI communication in mode 0
  SPI.setClockDivider(SPI_CLOCK_DIV16); // configuration of clock at 1MHz


  pinMode(CS, OUTPUT); //configure pin connected to chip select as output
  pinMode(IRPIN, INPUT); //read the digital input from the linetracker sensor

  client.setServer(mqtt_server, 1883);
  startMillis = millis();
  }

void loop() {
  if (!client.connected()) {
    reconnect();
  }

  client.loop();
  imu();
  lineTracker();

  currentMillis = millis();

    if ((currentMillis-startMillis) >= period){
      lightSensor();
      delay(10);
      currentMillis = 0;
      startMillis = millis();
    }
  
  delay(500);

  //ESP.deepSleep(10e6);
}