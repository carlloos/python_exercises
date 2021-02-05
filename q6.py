#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:02:05 2021
"""

def ModifyTuplesList(lista, y = 0):
    
    while y < len(lista):
        z = lista[y]
        z = list(z)
        z[-1] = 100
        z = tuple(z)
        lista[y] = z
        y +=1
        
    
    

def InsertTuple(lista,m,i = 0):
    tupla= ()
    while i < m:
        k = int(input("Digite um elemento para a tupla: "))
        tupla = tupla + (k ,)
        i +=1
    return tupla
    
    
    
    
lista = []

n = int(input("Digite o tamanho da lista: "))


m = int(input("Digite o tamanho das tuplas: "))


j =0

while j < n:
    t = InsertTuple(lista,m)
    lista.append(t)
    j+=1
    
    
ModifyTuplesList(lista)
print(lista)
