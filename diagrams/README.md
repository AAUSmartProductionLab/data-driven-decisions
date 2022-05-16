# Technical Documentation
Here is the documentation for the IIoT Box and the ESP Boxes

## Electrical Diagrams
Below you can see diagrams of the two ESP Box types. These show the connections between the various components and the requisite 
voltage levels to assist in troubleshooting of the ESP Boxes. 

### ESP Box Type 01
The Type 01 ESP Box has both an RFID reader and DHT11 connected, which are supplied separately via the 5V and 3.3V pins on the ESP.
This type utilises the ESP's built-in DeepSleep functionality, which requires that the RST pin be connected to the D0 pin, in order 
for the ESP to wake-up without external intervention. Below can be seen the electrical diagram for the Type 01 ESP Box.

![Electrical Diagram of the ESP Box Type 01](https://github.com/AAUSmartProductionLab/data-driven-decisions/blob/f5fb6779eec363ef93358ef505e5dab8b638c0d8/diagrams/ESP%20Box%2001.png)

The below table summarises the pin connections for the Type 01:

| ESP Pin | Conductor Colour |   Target   | Comment |
|---------|------------------|------------|---------|
| D0      |        ---       | RST        |  Function not currently used     |
| Tx      |                  | Tx (RFID)  |         |
| Rx      |                  | Rx (RFID)  |         |
| 5V      |       Red        | Vcc (RFID) |         |
| GND     |       Black      | GND        |         |
| D5      |       Blue       | S (DHT11)  |         |
| 3.3V    |       Red        | + (DHT11)  |         |
| GND     |       Black      | - (DHT11)  |         |

### ESP Box Type 02
The Type 02 ESP Box has an IMU and an industrial diffuse/through-beam PNP-type optosensor connected, which are supplied separately 
via the 3.3V and 5V pins on the ESP. The optosensor is supplied 12V via a 5V/12V Boost Regulator. This type does not utilise the 
ESP's built-in DeepSleep functionality. Below can be seen the electrical diagram for the Type 02 ESP Box.


![Electrical Diagram of the ESP Box Type 02](https://github.com/AAUSmartProductionLab/data-driven-decisions/blob/f5fb6779eec363ef93358ef505e5dab8b638c0d8/diagrams/ESP%20Box%2002.png)

The below table summarises the pin connections for the Type 02:

| ESP Pin | Conductor Colour |        Target        | Comment |
|---------|------------------|----------------------|---------|
| D0      |       Green      | SCL (IMU)            |         |
| D1      |       Blue       | SDA (IMU)            |         |
| 3.3     |       Red        | Vcc (IMU)            |         |
| GND     |       Black      | GND (IMU)            |         |
| D4      |       White      | o1 (Optoisolator)    |         |
| 3.3V    |       Red        | Vcc (Optoisolator)   |         |
| GND     |       Black      | GND (Optoisolator)   |         |
| 5V      |       Red        | In+ (5V/12V Step-up) |         |
| GND     |       Black      | In- (5V/12V Step-up) |         |

Furthermore, the pin connections for the optoisolator board are summmarised below:

| Optoisolator Pin | Conductor Colour |                  Target                  | Comment |
|------------------|------------------|------------------------------------------|---------|
| 1+               |      Black       | Pin 4 (Optosensor)                       |         |
| 1-               |      Blue        | Pin 3 (Optosensor)/ GND (5V/12V Step-up) |         |
| 2+               |      Brown       | Pin 2 (Optosensor)                       | Function currently not in use (can be connected) |

Finally, the pin connections for the Boost Regulator are summarised below:

| 5V/12V Step-up Converter Pin | Conductor Colour |                Target                 | Comment |
|------------------------------|------------------|---------------------------------------|---------|
| In+                          |      Red         | 5V (ESP)                              |         |
| In-                          |      Black       | GND (ESP)                             |         |
| Out+                         |      White       | Pin 1 (Optosensor)                    |         |
| Out-                         |      Blue        | Pin 3 (Optosensor)/ 1- (Optoisolator) |         |


## Communication Diagrams
The below diagram illustrates the data flow from sensors to user, to assist in troubleshooting data-collection
issues. 

![IIoT Box Data Flow](https://github.com/AAUSmartProductionLab/data-driven-decisions/blob/f5fb6779eec363ef93358ef505e5dab8b638c0d8/diagrams/Dataflow%20Diagram%20IIoT%20Box.png)


