#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:42:59 2021

"""

def MaiorNumero(lista, x):
    
    for j in lista:
        if j > x:
            x = j
            
    print("O maior número na lista é: {}".format(x))

lista = []
i = 0
n = int(input("Digite o tamanho da lista: "))

while i < n:
    
    x = int(input("Digite um número: "))
    lista.append(x)
    i+=1
    
x = 0 
  
MaiorNumero(lista,x)
