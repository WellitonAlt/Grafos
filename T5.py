import random as rm
import math
import networkx as nx
import numpy as np


def Twice_Around(G):
    #Cira uma MST
    MST = nx.minimum_spanning_tree(G)
    #Gera um SuperGrafico
    SMST = nx.MultiGraph()
    #Duplica as arestas
    for edge in MST.edges():
        SMST.add_edge(edge[0], edge[1], weight = G[edge[0]][edge[1]]['weight'])
        SMST.add_edge(edge[0], edge[1], weight = G[edge[0]][edge[1]]['weight'])

    #Da onde vai começa o tour
    Ini = [2,4,6,8,10,12,14,16,18,20]
    L = []
    #Gera os 10 ciclos Hamiltoniano
    for i in range(0, len(Ini)):
        #Gera o tour de Euler
        Eulirian_tour = nx.eulerian_circuit(SMST, source = Ini[i])
        Ciclo_Hamilt = []
        #Remove as repetiçoes e gera o cilco Hamiltoniano
        for edge in Eulirian_tour:
            if edge[0] not in Ciclo_Hamilt:
                Ciclo_Hamilt.append(edge[0])
            if edge[1] not in Ciclo_Hamilt:
                Ciclo_Hamilt.append(edge[1])

        Ciclo_Hamilt.append(Ciclo_Hamilt[0])
        #Calcula o peso do cliclo
        Peso = 0
        for i in range(0, len(Ciclo_Hamilt)-2):
            Peso = Peso + G.get_edge_data(Ciclo_Hamilt[i], Ciclo_Hamilt[i+1])['weight']

        #Exibe o ciclo
        print("Ciclo Hamiltoniano: ", Ciclo_Hamilt)
        print("Peso: ", Peso)
        #Lista com os pesos e os ciclos
        L.append(Peso)
        L.append(Ciclo_Hamilt)
    return L

def Classifica(L):
    MP = [0,0,0] #Lista com os melhores ciclos
    MC = [0,0,0]
    PP = [0,0,0]
    PC = [0,0,0] #Lista com os piores ciclos

    #Procura os 3 melhores
    for i in range (0, 3):
        cont = 0
        pos = 0
        Maior = 0
        print(len(L))

        while cont < len(L):
             if Maior < L[cont]:
                Maior = L[cont]
                pos = cont
             cont = cont + 2
        MP[i] = L[pos]
        MC[i] = L[pos+1]
        print(MP)
        print(MC)
        L.remove(MP[i])
        L.remove(MC[i])

    #Procura os 3 piores
    for i in range (0, 3):
        cont = 0
        pos = 0
        Menor = math.inf
        print(len(L))

        while cont < len(L):
             if Menor > L[cont]:
                Menor = L[cont]
                pos = cont
             cont = cont + 2
        PP[i] = L[pos]
        PC[i] = L[pos+1]
        print(PP)
        print(PC)
        L.remove(PP[i])
        L.remove(PC[i])

    #Exibe o resultaodo
    print("Melhores")
    cont = 0
    while cont < len(MP):
        print("Peso: ", MP[cont])
        print("Cliclo Hamiltoniano: ", MC[cont])
        cont = cont + 1

    print("Piores")
    cont = 0
    while cont < len(PP):
        print("Peso: ", PP[cont])
        print("Cliclo Hamiltoniano: ", PC[cont])
        cont = cont + 1

    return 0

#Trasforma a Matriz em um grafo
A = np.loadtxt('Matriz.txt')
G = nx.from_numpy_matrix(A)

L = Twice_Around(G)
Classifica(L)