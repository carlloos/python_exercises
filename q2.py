#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:53:23 2021

@author: carllos
"""

def FirstZeroIndex(lista,j):
     
    while True :
        
        if j >= len(lista):
            print("Essa lista não possui zero")
            break
        if lista[j] == 0:
            print("O index do primeiro zero é : {}".format(j))
            break
                
        else:
            j+=1
        

lista = []
i = 0
n = int(input("Digite o tamanho da lista: "))

while i < n:
    
    x = int(input("Digite um número: "))
    lista.append(x)
    i+=1

j=0
FirstZeroIndex(lista,j)
    
