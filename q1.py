#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:40:41 2021

"""
def comparation():
    for n in list1:
        x =+ n
    for m in list2:
        y =+ m
    
    if x < y:
        print("A soma dos numeros da primeira lista é menor do que os da segunda")
    elif x == y:
        print("As duas listas tem somas iguais")
    else:
        print("A soma dos numeros da primeira lista é maior do que os da segunda")


i = int(input("Digite o tamanho da primeira lista: "))

list1 = list(range(i))
j = int(input("Digite o tamanho da segunda lista: "))

list2 = list(range(j))

x = 0
y = 0

comparation()
