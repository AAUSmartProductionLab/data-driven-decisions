# IIoT Box Start-up guide

This guide will describe the step-by-step process to set up the IIoT Box on the shopfloor. 

## Initial Steps

   1. Power up the box using the USB-A to USB-A cable provided in the box.
   2. Connect to the WiFi Access Point with that has the same name as the IIoT Box (e.g. iiot_box_2).
   3. Once connected, the status of the raspberry pi can be check visiting: `10.3.141.1` in the browser. The credentials are: **username: iiot_case_2** and **password: robotlab**. From the dashboard it can be seen what devices are connected to the IIoT Box this could for example be the sensor boxes. These will appear with the host name ESP followed by a 6 number/letter ID e.g. **ESP-9003A5** or **ESP-90019F**.
   4. If everything is up and running (see: [Troubleshooting](TROUBLESHOOTING.md)) Node-RED can be accessed through port 1880. So go to the address `10.3.141.1:1880`.
   5. In Node-RED data can be accessed, analyzed and formatted such that it can be used in a dashboard or for storing. For a more in depth guide on Node-RED check the guide here (see: [Node-RED Guide](node-red/README.md)).

## Contents of the IIoT Box

## More Guides and Descriptions

- [Node-RED Guide](node-red/README.md)
- [Communication and Electrical Diagrams](diagrams/README.md)
- [Sensor Descriptions and Datasheets](sensors/README.md)
- [Code](code/README.md)
