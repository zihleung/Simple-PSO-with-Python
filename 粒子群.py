# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:38:35 2017

@author: user
"""

#求 x0^2+(x1-1)^2+(x2-2)^2+(x3-3)^2+(x4-4)^2的最小值.
import random
import math
import matplotlib.pyplot as plt
BirdNumber = 30
Size = 5
Position = []
Speed = []
Mybest = []
Globalbest = []
c1=2
c2=2
a=[]
b=[]
#初始化种群位置,种群速度:
for i in range(BirdNumber):
    for j in range(Size):
        a.append(random.uniform(-100,100))
        b.append(random.uniform(-100,100))
    Position.append(a)
    Speed.append(b)
#每个粒子的目标值:
def target(list):
    result=0
    for i in range(len(list)):
        result=result+math.pow(list[i]-i,2) 
    return result    
#寻找更新后的整体最好值:
def FindGlobalbest(Position):
    a=[]
    Globalbest=[]
    for i in range(BirdNumber):
        a.append(target(Position[i]))
    Globalbest=Position[a.index(min(a))]
    return Globalbest
#更新位置,速度:
def gengxin(Globalbest,Mybest,Position,Speed,w):
    d=[]
    e=[]
    NewSpeed=[]
    NewPosition=[]
    #更新速度:
    for j in range(BirdNumber):
        for k in range(Size):
            c=w*Speed[j][k]+c1*random.random()*(Mybest[j][k]-Position[j][k])+c2*random.random()*(Globalbest[k]-Position[j][k])
            if c>20:
                c=20
            if c<-20:
                c=-20
            d.append(c)
        NewSpeed.append(d)
        d=[]
    #更新位置:
    for i in range(BirdNumber):
        for j in range(Size):
            e.append(Position[i][j]+NewSpeed[i][j])
        NewPosition.append(e)
        e=[]
    #更新个体最好值:
    for i in range(BirdNumber):
        if target(NewPosition[i])<target(Mybest[i]):
            Mybest[i]=NewPosition[i]
    #更新群体最好值:
    for i in range(BirdNumber):
        if target(Globalbest)>target(NewPosition[i]):
            Globalbest=NewPosition[i]            
    return Globalbest,Mybest,NewPosition,NewSpeed
Mybest=Position
Globalbest=FindGlobalbest(Position)
w=0
quxian=[]
for i in range(200):
    w=0.9-(0.9-0.4)*i/100
    Globalbest,Mybest,Position,Speed=gengxin(Globalbest,Mybest,Position,Speed,w)
    print(Globalbest)
    print(target(Globalbest),'\n')
    quxian.append(target(Globalbest))  
plt.plot(quxian)

