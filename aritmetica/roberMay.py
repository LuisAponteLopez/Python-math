#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:47:14 2019

@author: luisapontelopez
"""
#Programa para demostrar comportamiento caotico

def main():
    print("Este programa demuestra comportamineto caotico")
    x = float(input("¨Entre un valor entre 0 y 1"))#te pide que le ponga algo
    k =float(input("¨Entre un valor entre 0 y 4"))
    n = int(input("entre el numero de repeticiones"))
    for i in range(n):#ciclo y range es la veces que queremos repetir 
        x = k*x*(1-x)
        print(x)
main() #ejecutar la funcion que definimo como def main():