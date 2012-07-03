#!/usr/bin/python
#
#Data port Synchronizer

import math
import numpy as np
import lgsm
import os

# loader, fom xde binaries, set path to modules used to access to xde modules
import loader
# dsimi.rtt : convert RTT::TaskContext * into a python object
import dsimi.rtt
# lgsm libraries
import rtt_interface as rtt
# deployer : loading ocl shared libraries
import deploy.deployer as ddeployer

synchronizer = None
TIME_STEP = 0.005

class PortSynchronizer(dsimi.rtt.Task):
	def __init__(self, task):
		super(PortSynchronizer, self).__init__(task)
		# flag for data reception
		self.dataFlag = {}

		# read value
		self.data = {}

		self.isReady = False

		self.portList = []

	def ready(self):
		if self.isReady:
			return True
		else:
			return False

	def checkAllFlag(self):
		for v in self.dataFlag.itervalues():
			if v==False:
				return False

		return True

	def updateHook(self):
		# if data has not yet been read
		for port in self.portList:
			if not self.dataFlag[port.getName()]:
				self.data[port.getName()], self.dataFlag[port.getName()] = port.read()

		# Check data flag, if all flags are true, all data are ready
		if self.checkAllFlag():
			self.isReady = True
			print self.getName()+" ready"
			for flagKeys in self.dataFlag.iterkeys():
				self.dataFlag[flagKeys] = False

	def startHook(self):
		pass

	def stopHook(self):
		pass

	def getData(self):
		if self.isReady:
			self.isReady = False
			return self.data
		else:
			print "Not Ready, returning previous value"
			return self.data

	def addPort(self,port_in):
		if isinstance(port_in, dsimi.rtt.InputPort):
			self.portList.append(port_in)
			self.isReady = False
			self.dataFlag[port_in.getName()] = False
		else:
			print "Not an InputPort"

def createTask():
	task = rtt.PyTaskFactory.CreateTask("syncTask")
	synchronizer = PortSynchronizer(task)
	setProxy(synchronizer)
	return synchronizer

def setProxy(_synchronizer):
	global synchronizer
	synchronizer = _synchronizer

def startTask():
	synchronizer.s.setPeriod(TIME_STEP)
	synchronizer.s.start()

