#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from guppy import hpy
import sys
def criargrafosaida(lista,registro):
    matriz=[]
    for i in range(0,len(lista)):
        vertice=[]
        for x in registro:
            if i==x[0]:
                vertice.append(x[1])
        matriz.append(vertice)
    return matriz   
def criargrafoentrada(lista,registro):
    matriz=[]
    for i in range(0,len(lista)):
        vertice=[]
        for x in registro:
            if i==x[1]:
                vertice.append(x[0])
        matriz.append(vertice)
    return matriz   


hp = hpy()
registro = []
registrosaida = []
registroentrada = []
lista= []
with open("grafo_mini.txt") as file:
    for linha in file:
        linha = linha.strip('\n')
        linha = linha.split(',')
        for reg in linha:
           if((reg in lista)==False):
               lista.append(reg)
        linha[0]=lista.index(linha[0])
        linha[1]=lista.index(linha[1])
        registro.append(linha)        
h = hp.heap()
#print len(lista)
print registro
print criargrafosaida(lista,registro)
print criargrafoentrada(lista,registro)

print(h) 
