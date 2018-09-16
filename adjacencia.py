#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from guppy import hpy
import sys
def criargrafosaida(lista,registro):
    matriz=[]
    for i in range(0,len(lista)):
        vertice=[]
        for x in registro:
            if lista[i]==x[0]:
                vertice.append(lista.index(x[1]))
        matriz.append(vertice)
    return matriz   
def criargrafoentrada(lista,registro):
    matriz=[]
    for i in range(0,len(lista)):
        vertice=[]
        for x in registro:
            if lista[i]==x[1]:
                vertice.append(lista.index(x[0]))
        matriz.append(vertice)
    return matriz   


hp = hpy()
registro = []
registrosaida = []
registroentrada = []
lista= []
with open("wiki_sp.txt") as file:
    for linha in file:
        linha = linha.strip('\n')
        linha = linha.split(',')
        registro.append(linha)
    for i in registro:
        for reg in i:
           if((reg in lista)==False):
               lista.append(reg)
h = hp.heap()
#print len(lista)
#print len(registro)
#print len(criargrafosaida(lista,registro))
print len(criargrafoentrada(lista,registro))

print(h) 
