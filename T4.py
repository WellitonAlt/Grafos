import random as rm
import matplotlib.pyplot as plt
import networkx as nx
import math


def Dijkstra(G, K):
    # Cria a lista de Ventices
    Q = []
    # Define infinito para a lista de prioridades e 0 para a raiz da arvore
    for i in G.nodes():
        G.node[i]['lambda'] = math.inf
        Q.append(G.node[i]['lambda'])
        G.node[i]['pi'] = None
    cont = 0
    Raizes = []
    # Saorteia as raizes de 1 a 3
    while cont < K:
        R = rm.randint(0, G.number_of_nodes() - 1)
        if Q[R] != 0:
            G.node[R]['lambda'] = 0
            Q[R] = 0
            Raizes.append(R)
            cont += 1

    print("R", Raizes)
    # Para todos os vertices faça
    for i in range(0, len(Q)):
        Menor = math.inf
        # Retorna o menor da lista
        for i in range(0, len(Q)):
            if Q[i] != -1:
                if Q[i] < Menor:
                    U = i
                    Menor = Q[i]

        # Retira o vertice da lista
        Q[U] = -1
        # Percorre os vizinhos do vertice e atualiza os valores de lambda e o predecessor
        for i in G.neighbors(U):
            if Q[i] != -1:
                Aux = G.node[i]['lambda']
                G.node[i]['lambda'] = min(G.node[i]['lambda'], (G.node[U]['lambda'] + G.get_edge_data(U,i)['value']))
                Q[i] = min(G.node[i]['lambda'], (G.node[U]['lambda'] + G.get_edge_data(U,i)['value']))

                if Aux != G.node[i]['lambda']:
                    G.node[i]['pi'] = U

    # Com base na tabela de predecessores cria a MST
    MST = nx.Graph()
    for i in range(0, len(Q)):
        MST.add_node(i,label = G.node[i]['label'])

    for i in range(0, len(Q)):
        if K == 1:
            if (i != Raizes[0]):
                MST.add_edge(i,G.node[i]['pi'])
        elif K == 2:
            if (i != Raizes[0]) and (i != Raizes[1]):
                MST.add_edge(i, G.node[i]['pi'])
        elif K == 3:
             if (i != Raizes[0]):
                 if (i != Raizes[1]):
                    if (i != Raizes[2]):
                        MST.add_edge(i, G.node[i]['pi'])
    return MST

G = nx.read_gml("football.gml")
K = 3 #Numero de raizes
MST = Dijkstra(G, K)

#Plota a MST
pos = nx.spring_layout(MST, k = 0.10, iterations=100)
nx.draw(MST, pos, with_labels = True)
plt.savefig("1")

