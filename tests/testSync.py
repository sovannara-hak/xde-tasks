import loader
import lgsm
import dsimi.rtt
import dsimi.interactive
import math
import numpy as np
import deploy
deploy.loadTypekitsAndPlugins()

import sys
import os
import inspect

deploy.loadTypekitsAndPlugins()
import deploy.deployer as ddeployer

import xdeTasksUtils.synchronizer

import rtt_interface
import agents.graphic.simple

graph=agents.graphic.simple.createAgent("graphic",0)

p1=graph.addCreateOutputPort("v1", "VectorXd")
p2=graph.addCreateOutputPort("v2", "VectorXd")
p3=graph.addCreateOutputPort("p3", "Displacementd")

p1_in=graph.addCreateInputPort("v1_in", "VectorXd", True)
p2_in=graph.addCreateInputPort("v2_in", "VectorXd", True)
p3_in=graph.addCreateInputPort("p3_in", "Displacementd", True)

sTask = xdeTasksUtils.synchronizer.createTask()

v1=lgsm.vectord(1,2,3)
v2=lgsm.vectord(1,2,4,9,2)
d3=lgsm.Displacementd()

p1.connectTo(p1_in)
p2.connectTo(p2_in)
p3.connectTo(p3_in)

sTask.addPort(p1_in)
sTask.addPort(p2_in)
sTask.addPort(p3_in)

xdeTasksUtils.synchronizer.startTask()

dsimi.interactive.shell()()
