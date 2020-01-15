#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:05:19 2019

@author: luisapontelopez
"""
import math
print("************************************************************************")
print("   Este programa calcula el punto medio , la distancia y la pendiente")
print("\n************************************************************************")

x1 ,y1 = eval(input("Entre la primera coordenada con una coma entre medio: "))
x2 ,y2 = eval(input("Entre la segunda coordenada con una coma entre medio: "))

puntomediox, puntomedioy = (x1+x2)/2 , (y1+y2)/2
puntomedio = ("( "+str(puntomediox)+" , "+str(puntomedioy)+" )")
print(puntomedio)
distancia= math.sqrt((x2-x1)**2+(y2-y1)**2)
pendiente = (y2 - y1)/(x2-x1)

print("\nRESULTADO:\npunto medio =",puntomedio,"\ndistancia = ",round(distancia,2), "\npendiente = ",round(pendiente,2))