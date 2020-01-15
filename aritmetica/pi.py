# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:29:18 2019

@author: Juan
"""
# este programa aproxima hasta el numero pi 
suma = -1
ecuacion = 0
for i in range(1,100,2):
    suma = -suma
    valor = i*suma
    print(valor)
    ecuacion = ecuacion + 4/valor
print(ecuacion)
