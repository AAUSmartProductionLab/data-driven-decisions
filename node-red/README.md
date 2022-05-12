# Node-RED Guide

This is a guide on how to use and understand the currently implemented Node-RED flows. This guide will only go through the basics briefly, so it is suggested to watch this YouTube guide to get a better understanding of Node-RED (see: [Video-Guide](https://www.youtube.com/watch?v=3AR432bguOY&ab_channel=OptoVideo)).

## The basics

Node-RED is a flowbased programming tool developed by IBM and is often times used to interface different programs and APIs with eachother. This feature is very useful, in the context of IoT and IIoT, since there are often many different devices that operate with different programming languages, interfaces and programs. Node-RED can then act as the glue tying all these technologies together.

Node-RED is accessed through a webinterface that is usually located on port `1880`. This means that if you type the IP-address of the device, running Node-RED, into the URL field in the browser followed by `:1880` it should open Node-RED. An example of this can be seen in the Figure 1.

![Figure](../figures/node-red-guide-1.png)
*Figure 1: Node-RED example flow*

Two of the most essential programming blocks can also be seen in the Figure 1.
