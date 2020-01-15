# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:26:50 2019

@author:Luis
"""
suma = 1
segundasuma = 0
numero = eval(input("que se valor te intesa saber de la serie sucesion de finonachi ?  "))
for i in range (numero-1):
    total = suma + segundasuma
    suma = segundasuma 
    segundasuma=total 

print(total)
 
