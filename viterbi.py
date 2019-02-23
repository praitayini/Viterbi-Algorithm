#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 16:34:53 2017

@author: praitayinikanakaraj
"""
#Implementing the Viterbi Algorithm
# The given observation space, state space, transition matrix, start probability,
# transition probability and emission probability are below
obSpace = ('High Fever', 'Cold', 'Vomit');
stateSpace = ('Heart Disease', 'Cold','Fever','Bronchitis','Food Posioning');
ob = ('High Fever','Cold','Vomit','High Fever','Cold','Cold','Cold','Cold');
trans_Matrix=[];
for j in range(0,len(stateSpace)):
    for i in range(0,len(stateSpace)):
        trans = stateSpace[i],stateSpace[j];
        trans_Matrix.append(trans);
print "Transition of the States is", trans_Matrix;
start_p = [0.2,0.2,0.2,0.2,0.2];
trans_p = [0,0.25,0.25,0.25,0.25],[0.1,0,0.4,0.4,0.1],[0.1,0.4,0,0.4,0.1],[0,0.2,0.7,0.05,0.05],[0.1,0.3,0.3,0,0.3];
emit_p = [0.05,0.05,0.05],[0.2,0.5,0.05],[0.5,0.05,0.2],[0.05,0.4,0],[0.2,0,0.7];
print ""
# Calculation for 1st observation 
# by multiplying the start probability and emission probability given present state
step_1 = [];
postion_step1 = [];
for i in range(0,len(stateSpace)):
    step1 = start_p[i] * emit_p[i][0];
    step_1.append(step1);
print "Observation 1 is:", step_1;
postion_step1 = step_1.index(max(step_1)); # finding the highest probability for the most likely state
print "Position of the highest value", postion_step1; 
print stateSpace[postion_step1], "when the observation is", ob[0];
print ""

# Calculation for 2nd observation 
# by multiplying the past probability, transition probability from that previous to current state
# and emission probability given present state
a = [];
step_2 = [];
postion_step2 = [];
for l in range(0,len(stateSpace)):
    for k in range(0,len(stateSpace)):
        a = step_1[k] * trans_p[k][l] * emit_p[l][1];
        step_2.append(a);
print "Observation 2 is:", step_2;
postion_step2 = step_2.index(max(step_2));
print "Position of the highest value", postion_step2;
t2=trans_Matrix[postion_step2];
print t2[0], "transits to", t2[1], "when the observation is", ob[1];
print ""

# to get the maximum of the past probability
max_value2 = [];
i = 0;
j = len(stateSpace);
while i < 21 or j < 26:
    x = max(step_2[i:j])
    max_value2.append(x);
    i = i+5;
    j= j+5; 

# Calculation for 3rd observation
# by multiplying the maximum past probability, transition probability from that previous to current state
# and emission probability given present state
b = [];
step_3 = [];
postion_step3 = [];
for l in range(0,len(stateSpace)):
    for k in range(0,len(stateSpace)):
        b = max_value2[k] * trans_p[k][l] * emit_p[l][2];
        step_3.append(b);
print "Observation 3 is:", step_3
postion_step3 = step_3.index(max(step_3));
print "Position of the highest value", postion_step3;
t3=trans_Matrix[postion_step3];
print t3[0], "transits to", t3[1], "when the observation is", ob[2];
print ""
# The same thing is done for the different observations
# The past probability and the emission probability given present state changes

# Calculation for 4th observation
max_value3 = [];
i = 0;
j = len(stateSpace);
while i < 21 or j < 26:
    x = max(step_3[i:j])
    max_value3.append(x);
    i = i+5;
    j= j+5; 
        
c = [];       
step_4 = [];
postion_step4 = [];
for l in range(0,len(stateSpace)):
    for k in range(0,len(stateSpace)):
        c = max_value3[k] * trans_p[k][l] * emit_p[l][0];
        step_4.append(c);
print "Observation 4 is:", step_4;
postion_step4 = step_4.index(max(step_4));
print "Position of the highest value", postion_step4;
t4=trans_Matrix[postion_step4];
print t4[0], "transits to", t4[1], "when the observation is", ob[3];
print ""
# Calculation for 5th observation
max_value4 = [];
i = 0;
j = len(stateSpace);
while i < 21 or j < 26:
    x = max(step_4[i:j])
    max_value4.append(x);
    i = i+5;
    j= j+5; 
    
d= [];        
step_5 = [];
postion_step5 = [];
for l in range(0,len(stateSpace)):
    for k in range(0,len(stateSpace)):
        d = max_value4[k] * trans_p[k][l] * emit_p[l][1];
        step_5.append(d);
print "Observation 5 is:", step_5;
postion_step5 = step_5.index(max(step_5));
print "Position of the highest value", postion_step5;
t5=trans_Matrix[postion_step5];
print t5[0], "transits to", t5[1], "when the observation is", ob[4];
print ""

# Calculation for 6th observation
max_value5 = [];
i = 0;
j = len(stateSpace);
while i < 21 or j < 26:
    x = max(step_5[i:j])
    max_value5.append(x);
    i = i+5;
    j= j+5; 
    
d= [];        
step_6 = [];
postion_step6 = [];
for l in range(0,len(stateSpace)):
    for k in range(0,len(stateSpace)):
        d = max_value5[k] * trans_p[k][l] * emit_p[l][1];
        step_6.append(d);
print "Observation 6 is:", step_6;
postion_step6 = step_6.index(max(step_6));
print "Position of the highest value", postion_step6;
t6=trans_Matrix[postion_step6];
print t6[0], "transits to", t6[1], "when the observation is", ob[5];
print ""

# Calculation for 7th observation
max_value6 = [];
i = 0;
j = len(stateSpace);
while i < 21 or j < 26:
    x = max(step_6[i:j])
    max_value6.append(x);
    i = i+5;
    j= j+5; 
    
d= [];        
step_7 = [];
postion_step7 = [];
for l in range(0,len(stateSpace)):
    for k in range(0,len(stateSpace)):
        d = max_value6[k] * trans_p[k][l] * emit_p[l][1];
        step_7.append(d);
print "Observation 7 is:", step_7;
postion_step7 = step_7.index(max(step_7));
print "Position of the highest value", postion_step7;
t7=trans_Matrix[postion_step7];
print t7[0], "transits to", t7[1], "when the observation is", ob[6];
print ""

# Calculation for 8th observation
max_value7 = [];
i = 0;
j = len(stateSpace);
while i < 21 or j < 26:
    x = max(step_7[i:j])
    max_value7.append(x);
    i = i+5;
    j= j+5; 
    
d= [];        
step_8 = [];
postion_step8 = [];
for l in range(0,len(stateSpace)):
    for k in range(0,len(stateSpace)):
        d = max_value7[k] * trans_p[k][l] * emit_p[l][1];
        step_8.append(d);
print "Observation 8 is:", step_8;
postion_step8 = step_8.index(max(step_8));
print "Position of the highest value", postion_step8;
t8=trans_Matrix[postion_step8];
print t8[0], "transits to", t8[1], "when the observation is", ob[7];
print ""

# The final answer
print "This reveals that the observations",ob, "were most likely generated by states", (stateSpace[postion_step1],t2[1],t3[1],t4[1],t5[1],t6[1],t7[1],t8[1]);



   
       
        
          
    
    
        
        
