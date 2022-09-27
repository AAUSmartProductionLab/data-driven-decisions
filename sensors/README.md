# Sensors
Several sensor options have been implemented, descriptions of which can be found below. The sensors that have currently (11/07/2022) been 
implemented are:

- Diffuse/Reflective Optosensor
- DHT11
- IMU

### Optosensor
The selected optosensor can be ustilised in either diffuse- or reflective-mode (diffuse-mode is default). In the former implemen-
-tation, the sensor functions as a normally open (NO) contact, and as a normally closed (NC) in the latter. In order to switch
modes, it is necessary to alter the sensing circuit configuration, to reconfigure the Node-RED flows and also to make use of re-
-flective material. It is advised that this reconfiguration be carried out by or in collaboration with the Lab Engineers or an-
-other, qualified person.

##### Code Function
The code for the Optosensor makes use of a state machine to monitor the status of the sensor relative to previous statuses. If no
 object is detected by the sensor, and no object has been previously detected, a '0' status is returned. If an object is then de-
 -tected, a '1' status is returned. If this object remains for a period of time, that is, continues to be detected, then a '2' 
 status is returned. When the object finally ceases to be detected, a '3' status is returned. This modality is inverted when the 
 sensor is configured in reflective-mode. The following table should serve to clarify:
 
| **Condition** | **Previous Condition** | **Diffuse-Mode** | **Reflective-Mode** |
|---|---|---|---|
| No Object | No Object | 0 | 2 |
| Object | No Object | 1 | 3 |
| Object | Object | 2 | 0 |
| No Object | Object | 3 | 1 |

The sensor condition is sampled on a 200ms basis as default, but this time can be successfully reduced to 50ms for fast moving sys-
-tems. Currently (27/09/2022), only 1 and 0 values are sent on to Node-RED. 

### DHT11
The DHT11 sensor is used to sample ambient temperature and humidity in an area. This sensor provides a humidity sensing range of 
20-80% with an accuracy of ±5%, and a temperature sensing range of 0-50°C with an accuracy of ±2°C. The sample rate is max 1Hz. 

##### Code Implementation
The current (11/07/2022) code implementation samples the temperature and humidity every 5 minutes, stores this data as a JSON-document 
on the ESP-box until 6 samples have been collected. This JSON-document is then published to the MQTT topic ESPBox1/DHT11. 

### IMU
The IMU sensor is used to gather acceleration and rotation data. An MPU6050 is currently (27/09/2022) used for this sensor. 

##### Code Implementation
The current (27/09/2022) code implementation samples the IMU data every 50ms and publishes this data immediately to the MQTT topic 
ESPBox2/imu. 
