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

class DataSwitch():
	def __init__(self):

		#List of known ports that constitutes the output of
		#components
   		self.portList = []

		#Switch list
		self.componentIn = []
		self.componentOut = []

		self.selectedCompIn = []
		self.selectedCompOut = []

		self.portListNames = []

		#is the data switch forwarding
		self.active = False

	def addPort(self, listPortId):
        for newPort in listPortId:
			self.portListNames.append(newPort)
		return

	def delPort(self, listPortId):
		for delPort in listPortId:
			self.portListNames.remove(delPort)
		return

	#Add a component to the switch list
	#check if the port are consistent with the other components
	#in the list
	#task: a new component that becomes a new state for the switch
	def addComponentIn(self, component):
		validPort = False

		#check if port list is empty
		if len(self.portListNames) == 0:
			print "Please define port list first using addPort(list)"
			return False

		newPortListNames = component.getPortNames()
		validPort = isIn(newPortListNames, self.portListNames)

		if validPort:
			self.componentIn.append(component)
		else
			print "Ports on component do not match"
			return False

    	return True

	def addComponentOut(self, component):
		validPort = False

		#check if port list is empty
		if len(self.portListNames) == 0:
			print "Please define port list first using addPort(list)"
			return False

		newPortListNames = component.getPortNames()
		validPort = isIn(newPortListNames, self.portListNames)

		if validPort:
			self.componentOut.append(component)
		else
			print "Ports on component do not match"
			return False

    	return True

	def switchIn(self, componentName):
		#self.selectedCompIn
		for component in componentIn:
 			if component.getName() == componentName:
				if len(self.selectedCompIn) != 0:
					self.selectedCompIn.pop()
            	self.selectedCompIn.append(component)
				return
			else
				print "Component "+componentName+" not found in list"
		return

	def switchOut(self, componentName):
		for component in componentOut:
 			if component.getName() == componentName:
				if len(self.selectedCompOut) != 0:
					self.selectedCompOut.pop()
            	self.selectedCompOut.append(component)
				return
			else
				print "Component "+componentName+" not found in list"
		return

	def connect(self):
		if len(self.selectedCompIn) != 0 and len(self.selectedCompOut) != 0:
			for component in self.componentIn:
            	if component.getName() == self.selectedCompIn[0]:
					compIn = component
					break
			for component in self.componentOut:
            	if component.getName() == self.selectedCompOut[0]:
					compOut = component
					break
			for portId in self.portListNames:
				compIn.getPort(portId).connectTo(compOut.getPort(portId))
		else
			print "Input Component or output component not selected"
			return False

		return

	#Disconnect all ports
	def disconnect(self):
		for component in self.componentIn:
			if component.getName() == self.selectedCompIn[0]:
				compIn = component
					break
		for portId in self.portListNames:
			compIn.getPort(portId).disconnect()
		return

	def removeComponent(self, componentId):
		pass

	#print state info of the switch
	#and component list
	def getState(self):
		if len(self.selectedCompIn) != 0:
			selectNameIn = self.selectedCompIn[0]
		if len(self.selectedCompOut) != 0:
			selectNameOut = self.selectedCompOut[0]

		for component in self.componentIn:
			if selectNameIn == component.getName()
				print "+ "+component.getName()+">"
			else
				print "- "+component.getName()+">"
		for component in self.componentOut:
			if selectNameOut == component.getName()
				print "+ >"+component.getName()
			else
				print "- >"+component.getName()
		return

	#forward portId to the output instead of the
	#default component's port
	def overide(self, portId):
		pass

