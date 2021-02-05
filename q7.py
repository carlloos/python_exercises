#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:55:51 2021

"""

dict1 = {'A': 1, 'B': 2, 'C':3}
print("Primeiro dicionário: {}".format(dict1))
dict2 = {'D': 4, 'E': 5, 'F': 6}
print("Segundo dicionário: {}".format(dict2))

dict1.update(dict2)

print("Os dois dicionários combinados: {}".format(dict1))
