#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EQ ORGANIZATION: https://www.lucidchart.com/documents/edit/c15a7865-f309-4d48-947f-f7b00ac05159/0

https://academic.oup.com/brain/article/137/8/2210/2847958#78872443

@TODOs
    plots
    fns
    connectivity
    
"""

from DyPy import dynsys as DS

class epileptorNode(object):
    def __init__(self): 
        pass
    
    def actionOnStep(self):
        pass
    
    
g=DS.Constant('\gamma',0.01)
t1=DS.Constant('\tau_1',1)
t2=DS.Constant('\tau_2',1)
    
y1=DS.Variable()
x1=DS.Variable()
z=DS.Variable()
y2=DS.Variable()
x2=DS.Variable()

#Seizure Spikes
#x1dot=y1-f1(x1,x2)-z+i_rest1
#y1dot=y0-5x1^2-y1

#Seizure State
#zdot=1/tau_0(4(x_1-x_0)-z)
    
#Between-Seizure Spikes
#x2dot=-y_2+x_2-x_2^3+I_rest2+0.002*g(x_1)-0.3*(z-3.5)
#y2dot=1/tau_2(-y_2+f_2(x_1,x_2))
    
#Activation Functions
#g(x) --ONLY USED WITH x_1 TO DETERMINE x_2
#f_1(x1,x2) --ONLY USED WITH x_1,x_2 TO DETERMINE x_1
#f_2(x2) --ONLY USED WITH x_2 TO DETERMINE y_2
        #x_1 y_1  z  x_2  y_2
#narray=([[0., 1, -1, 0., 0.],#+i_rest1-f1(x1,x2)
#         [-5*(lambda x:x^2), -1, 0., 0., 0.],#+y0, square the x_1?
#         [4., 0., -1, 0., 0.],#(-4x_0)/tau_0
#         [0., 0., 0., 1, -1],
#         [0., 0., 0., 0., 0.]])