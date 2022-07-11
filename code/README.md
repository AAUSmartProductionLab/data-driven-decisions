# Code
In this directory, the various code pieces that are used by the Raspberry Pi and the ESP-boxes can be found.
The contents of each folder are:

- **cpp:** This folder contains cpp-files for each ESP-box (1 & 2), they have been developed with PlatformIO using the Arduino framework.
           There is also a folder condtaining code for a wiegand-based RFID-reader.
- **node-red:** This folder contains JSON-files for the exported flows from Node-RED running on the Raspberry Pi. The currently hosted
            flows include:
            - Data Input
            - Dashboard
            - Datalog Download
- **python:** This folder contains a python script which governs the display for the Raspberry Pi touch-screen, as well as .png-files for
           this. 

