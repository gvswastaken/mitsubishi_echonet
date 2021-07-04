#!/usr/bin/env python3
import mitsubishi_echonet as mit
import time
from pprint import pprint

mit.ENL_MULTICAST_ADDRESS = "10.0.0.1"

echonet_objects = False
# Discover HVAC Echonet objects
while echonet_objects == False:
    print("Discovering Anything..")
    echonet_objects = mit.discover()

for instance in echonet_objects:
   
   if isinstance(instance, mit.HomeSolarPower):
       pprint(instance.getOperationalStatus())
       pprint(instance.getMeasuredCumulPower())
       pprint(instance.getMeasuredInstantPower())
   
   if isinstance(instance, mit.StorageBattery):
       pprint(instance.getOperationalStatus())
       pprint(instance.getRemainingStoredElectricity3())
       pprint(instance.getWorkingOperationStatus())

   #print(node.getControllerID())
   #print(node.getNumDevicesControlled())
   
   #print(node.update())
   # aircon.on()
  # print(node.getAirflowVert())
   # print(node.getAutoDirection())
    #print(node.getSwingMode())

   # node.setSwingMode('vert')
   # node.setSwingMode('not-used')

   # node.setAirFlowVert('central')

   # print("Getting current operational parameters")
   # print(aircon.update())
   # aircon.setFanSpeed('medium-low')

   # print("Getting outdoor temperature")
   # print(aircon.getOutdoorTemperature())
