# IIoT Box Start-up guide

This guide will describe the step-by-step process to set up the IIoT Box on the shopfloor.

## Initial Steps

   1. Power up the box using the USB-A to USB-A cable provided in the box.
   2. Connect to the WiFi Access Point with that has the same name as the IIoT Box (e.g. iiot_box_2).
   3. Once connected, the status of the raspberry pi can be check visiting: `10.3.141.1` in the browser. The credentials are: **username: iiot_case_2** and **password: robotlab**. From the dashboard it can be seen what devices are connected to the IIoT Box this could for example be the sensor boxes. These will appear with the host name ESP followed by a 6 number/letter ID e.g. **ESPBox1** or **ESPBox2**.
   4. If everything is up and running (see: [Troubleshooting](TROUBLESHOOTING.md)) Node-RED can be accessed through port 1880. So go to the address `10.3.141.1:1880` in the browser.
   5. In Node-RED data can be accessed, analyzed and formatted such that it can be used in a dashboard or for storing. For a more in depth guide on Node-RED check the guide here (see: [Node-RED Guide](node-red/README.md)).

---

## Contents of the IIoT Box

The IIoT box contains a Raspberry Pi 3B/3B+ that is used for setting up the access point and for storing the data from the sensor boxes. The IIoT box comes a 7-inch touch display, which can be used for debugging and visualization purposes. The IIoT box also comes with two sensor boxes. These sensor boxes uses a Wemos D1 Mini Pro ESP8266 microcontroller for collection and sending of data from the sensors. The exact sensors and their respective datasheets can be found in the folder [Sensor Descriptions and Datasheets](sensors/README.md).

---

## Usernames and Passwords

|                 | IIoT_Box_1  | IIoT_Box_2  | IIoT_Box_3  | IIoT_Box_4  |
|-----------------|-------------|-------------|-------------|-------------|
| Username        | pi          | pi          | pi          | pi          |
| Password        | robotlab    | robotlab    | robotlab    | robotlab    |
| SSID(WiFi Name) | iiot_case_1 | iiot_case_2 | iiot_case_3 | iiot_case_4 |
| WiFi Password   | robotlab    | robotlab    | robotlab    | robotlab    |
| Raspap username | admin       | admin       | admin       | admin       |
| Raspap password | robotlab    | robotlab    | robotlab    | robotlab    |

---

## More Guides and Descriptions

- [Node-RED Guide](node-red/README.md)
- [Communication and Electrical Diagrams](diagrams/README.md)
- [Sensor Descriptions and Datasheets](sensors/README.md)
- [Troubleshooting](TROUBLESHOOTING.md)
- [Code](code/README.md)
