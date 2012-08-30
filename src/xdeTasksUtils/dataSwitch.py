#!/usr/bin/python
#
#Data switch module

import math
import numpy as np
import lgsm
import os

from misc import isIn

# loader, fom xde binaries, set path to modules used to access to xde modules
import loader
# dsimi.rtt : convert RTT::TaskContext * into a python object
import dsimi.rtt
# lgsm libraries
import rtt_interface as rtt
# deployer : loading ocl shared libraries
import deploy.deployer as ddeployer

class DataSwitch(dsimi.rtt.Task):
	def __init__(self, task):
		super(DataSwitch, self).__init__(task)

		#List of known ports that constitutes the output of
		#components
   		self.portList = []
		self.readPortList = []
		self.portListNames = []

		#Switch list
		self.componentList = []

	#def updatePortListNames:
	#	for port in self.portList:
	#		self.portListNames.append(port.getName())
	#	return

	#Add a component to the switch list
	#check if the port are consistent with the other components
	#in the list
	#task: a new component that becomes a new state for the switch
	def addComponent(self, task):
		validPort = False
		#check if list is empty

		newPortListNames = task.getPortNames()
		if len(componentList) == 1: #list was empty
			self.portListNames.append(newPortListNames)

			#creation of output ports
			for portName in newPortListNames:
				port = task.getPort(portName)
				portType = port.getTypeInfo()
				self.portList.append(self.addCreateOutputPort(port.getName(), portType.getTypeName()))
				self.readPortList.append(self.addCreateInputPort(port.getName()+"_in", portType.getTypeName(), True))
			validPort = True
		else
			#check if port list is consistent
			#with the port of the new component
			validPort = isIn(newPortListNames, self.portListNames)

		if validPort:
			self.componentList.append(task)
		else
			print "Ports on component do not match"
			return False

    	return True

	#Disconnect all ports
	def disconnect(self):
		for port in self.portList:
			port.disconnect()

		return

	def removeComponent(self, componentId):
		pass

	def switch(self, componentId):
		pass

	#print state info of the switch
	#and component list
	def getState(self):
		pass

	#forward portId to the output instead of the
	#default component's port
	def overide(self, portId):
		pass

	def write(self, portId):
		pass

	def read(self, portId):
		pass



