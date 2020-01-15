#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:07:44 2019

@author: luisapontelopez
"""

import math

a = eval(input("Entre el coenficiente a: "))
b = eval(input("Entre el coenficiente b: "))
c = eval(input("Entre el coenficiente c: "))

x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

print("\nLas soluciones son \n x = ",x1," ; ",x2)