# Technical Documentation
Here is the documentation for the IIoT Box and the ESP Boxes

## Electrical Diagrams
Below you can see diagrams of the two ESP Box types. These show the connections between the various components and the requisite 
voltage levels to assist in troubleshooting of the ESP Boxes. 

### ESP Box Type 01
The Type 01 ESP Box has both an RFID reader and DHT11 connected, which are supplied separately via the 5V and 3.3V pins on the ESP.
This type utilises the ESP's built-in DeepSleep functionality, which requires that the RST pin be connected to the D0 pin, in order 
for the ESP to wake-up without external intervention. Below can be seen the electrical diagram for the Type 01 ESP Box.

![Electrical Diagram of the ESP Box Type 01](diagrams/ESP Box 01.png)

The below table summarises the pin connections for the Type 01:

| ESP Pin | Colour Code |   Target   | Comment |
|---------|-------------|------------|---------|
| D0      |             | RST        |         |
| Tx      |             | Tx (RFID)  |         |
| Rx      |             | Rx (RFID)  |         |
| 5V      |             | Vcc (RFID) |         |
| GND     |             | GND        |         |
| D5      |             | S (DHT11)  |         |
| 3.3V    |             | + (DHT11)  |         |
| GND     |             | - (DHT11)  |         |

### ESP Box Type 02
The Type 02 ESP Box has an IMU and an industrial diffuse/through-beam PNP-type optosensor connected, which are supplied separately 
via the 3.3V and 5V pins on the ESP. The optosensor is supplied 12V via a 5V/12V Boost Regulator. This type does not utilise the 
ESP's built-in DeepSleep functionality. Below can be seen the electrical diagram for the Type 02 ESP Box.


![Electrical Diagram of the ESP Box Type 02](diagrams/ESP Box 02.png)

The below table summarises the pin connections for the Type 02:

| ESP Pin | Colour Code |        Target        | Comment |
|---------|-------------|----------------------|---------|
| D0      |             | SCL (IMU)            |         |
| D1      |             | SDA (IMU)            |         |
| 3.3     |             | Vcc (IMU)            |         |
| GND     |             | GND (IMU)            |         |
| D4      |             | o1 (Optoisolator)    |         |
| 3.3V    |             | Vcc (Optoisolator)   |         |
| GND     |             | GND (Optoisolator)   |         |
| 5V      |             | In+ (5V/12V Step-up) |         |
| GND     |             | In- (5V/12V Step-up) |         |

Furthermore, the pin connections for the optoisolator board are summmarised below:

| Optoisolator Pin | Colour Code |                  Target                  | Comment |
|------------------|-------------|------------------------------------------|---------|
| 1+               |             | Pin 4 (Optosensor)                       |         |
| 1-               |             | Pin 3 (Optosensor)/ GND (5V/12V Step-up) |         |

Finally, the pin connections for the Boost Regulator are summarised below:

| 5V/12V Step-up Converter Pin | Colour Code |                Target                 | Comment |
|------------------------------|-------------|---------------------------------------|---------|
| In+                          |             | 5V (ESP)                              |         |
| In-                          |             | GND (ESP)                             |         |
| Out+                         |             | Pin 1 (Optosensor)                    |         |
| Out-                         |             | Pin 3 (Optosensor)/ 1- (Optoisolator) |         |


## Communication Diagrams
The below diagram illustrates the data flow from sensors to user, to assist in troubleshooting data-collection
issues. 

![IIoT Box Data Flow](diagrams/Dataflow Diagram IIoT Box.png)
