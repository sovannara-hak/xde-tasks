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

		#is the data switch forwarding
		self.active = False

		#Switch list
		self.componentList = []

	#Add a component to the switch list
	#check if the port are consistent with the other components
	#in the list
	#task: a new component that becomes a new state for the switch
	def addComponent(self, component):
		validPort = False
		#check if list is empty

		newPortListNames = component.getPortNames()
		if len(componentList) == 1: #list was empty
			self.portListNames.append(newPortListNames)

			#creation of output ports
			for portName in newPortListNames:
				port = component.getPort(portName)
				portType = port.getTypeInfo()
				dataSwitchOutPort = self.addCreateOutputPort(port.getName(), portType.getTypeName())
				self.portList.append(dataSwitchOutPort)
				#creation of input port that will be used to forward
				#data from a component to the data switch
				dataSwitchInPort = self.addCreateInputPort(port.getName()+"_in", portType.getTypeName(), True)
				self.readPortList.append(dataSwitchInPort)

			validPort = True
		else
			#check if port list is consistent
			#with the port of the new component
			validPort = isIn(newPortListNames, self.portListNames)

		if validPort:
			self.componentList.append(component)
		else
			print "Ports on component do not match"
			return False

    	return True

	#Disconnect all ports
	def disconnect(self):
		for port in self.portList:
			port.disconnect()
		return

	def forward(self)
		#read output from data switch input
		#write data in data switch output
		for portName in portListNames:
        	data = self.getPort(portName+"_in").read()
			self.getPort(portName).write(data[0])
		return

	def removeComponent(self, componentId):
		pass

	def connect(self):
		for port in portListNames:
			self.getPort(portListNames+"_in").connectTo(self.selectComponent.getPort(portListNames))
		return

	def switch(self, componentName):
		global self.selectComponent

		self.disconnect()
		for component in componentList:
 			if component.getName() == componentName:
            	self.selectComponent = component
                #connection of component Out to data switch in
				self.connect()
				return
			else
				print "Component "+componentName+" not found in list"
		return

	#print state info of the switch
	#and component list
	def getState(self):
		if not self.selectComponent:
			selectName = self.selectComponent.getName()

		for component in self.componentList:
			if selectName == component.getName()
				print "+ "+component.getName()
			else
				print "- "+component.getName()
		return

	#forward portId to the output instead of the
	#default component's port
	def overide(self, portId):
		pass

	def updateHook(self):
		pass

	def startHook(self):
		pass

	def stopHook(self):
		pass


