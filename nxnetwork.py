import networkx as nx
from guppy import hpy
G = nx.DiGraph()
hp = hpy()
registro = []
with open("grafo_mini.txt") as file:
    for linha in file:
        linha = linha.strip('\n')
        linha = linha.split(',')
        registro.append(linha)
    G.add_edges_from(registro)
print G.adj
h = hp.heap()
print(h) 
