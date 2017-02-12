import random as rm
import matplotlib.pyplot as plt
import networkx as nx
import math


def prim(G, R):
    #Cria a lista de Arestas
    Q = []
    #Define infinito para a lista de prioridades e 0 para a raiz da arvore
    for i in G.nodes():
        G.node[i]['lambda'] = math.inf
        Q.append(G.node[i]['lambda'])
        G.node[i]['pi'] = None
    G.node[R]['lambda'] = 0
    Q[R] = 0

    #Para todos os vertices faça
    for i in range(0, len(Q)):
        #Retorna o menor da lista
        Menor = math.inf
        for i in range(0, len(Q)):
            if Q[i] != -1:
                if Q[i] < Menor:
                    U = i
                    Menor = Q[i]
        #Retira o vertice da lista
        Q[U] = -1
        #Percorre os vizinhos do vertice e atualiza os valores de lambda e o predecessor
        for i in G.neighbors(U):
            if Q[i] != -1:
                Aux = G.node[i]['lambda']
                G.node[i]['lambda'] = min(G.node[i]['lambda'], G.get_edge_data(U,i)['value'])
                Q[i] = min(G.node[i]['lambda'], G.get_edge_data(U,i)['value'])
                if Aux != G.node[i]['lambda']:
                    G.node[i]['pi'] = U
    MST = nx.Graph()
    #Com base na tabela de predecessores cria a MST
    for i in range(0, len(Q)):
        MST.add_node(i,label = G.node[i]['label'])

    for i in range(0, len(Q)):
        if (i != R):
            MST.add_edge(i,G.node[i]['pi'])

    return MST

G = nx.read_gml("football.gml")
#Escolhe uma raiz aleatoria
R = rm.randint(0,G.number_of_nodes()-1)
MST = prim(G, R)

#Plota a MST
pos = nx.spring_layout(MST, k = 0.10, iterations=100)
nx.draw(MST, pos, with_labels = True)
plt.savefig("Prim")

