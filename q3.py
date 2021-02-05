#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:09:48 2021

"""

def ListConcat(lista):
    
    lista_concatenada = ''
    for y in lista:
        lista_concatenada = lista_concatenada + y
        
    #lista_concatenada = ' '.join(lista)
    
    print(lista_concatenada)
    

lista = []
i = 0
n = int(input("Digite o tamanho da lista: "))

while i < n:
    
    x = str(input("Digite uma palavra: "))
    lista.append(x)
    i+=1

ListConcat(lista)
