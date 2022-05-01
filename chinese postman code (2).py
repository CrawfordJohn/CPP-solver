# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 20:08:28 2021

@author: John Crawford
"""
from GraphVisualization2 import GraphVisualization
from Fluery import Graph
G = GraphVisualization()
  
graph4 = [[0,0,1,0],
          [0,0,1,1],
          [1,1,0,1],
          [0,1,1,0]]


graph5 = [[0,1,0,0,0],
          [1,0,0,0,1],
          [0,0,0,1,1],
          [0,0,1,0,1],
          [0,1,1,1,0]]



graph3 = [[0,1,1,1,1],
          [1,0,1,0,0],
          [1,1,0,0,0],
          [1,0,0,0,1],
          [1,0,0,1,0]]

graph6 =                 [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
                       [4, 0, 8, 0, 0, 0, 0, 11, 0], 
                        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
                        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
                        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
                        [0, 0, 4, 0, 10, 0, 2, 0, 0], 
                        [0, 0, 0, 14, 0, 2, 0, 1, 6], 
                        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
                        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
                    ]; 

graph2 =                [[0, 3, 1, 0, 5, 0], 
                        [3, 0, 0, 1, 0, 6], 
                        [1, 0, 0, 0, 2, 0], 
                        [0, 1, 0, 0, 0, 1], 
                        [5, 0, 2, 0, 0, 4], 
                        [0, 6, 0, 1, 4, 0], 
                         
                    ]; 
graph7 = [[0, 199, 101, 586, 570, 472, 496, 473], [199, 0, 98, 548, 601, 510, 450, 470], [101, 98, 0, 558, 577, 481, 462, 460], [586, 548, 558, 0, 202, 216, 97, 133], [570, 601, 577, 202, 0, 97, 232, 147], [472, 510, 481, 216, 97, 0, 202, 102], [496, 450, 462, 97, 232, 202, 0, 100], [473, 470, 460, 133, 147, 102, 100, 0]]


def sum_edges(graph):
    w_sum = 0
    l = len(graph)
    for i in range(l):
        for j in range(i,l):
            w_sum += graph[i][j]
    return w_sum
            
def dijktra(graph, source, dest):
    shortest = [0 for i in range(len(graph))]
    selected = [source]
    l = len(graph)
    #Base case from source
    inf = 10000000
    min_sel = inf
    for i in range(l):
        if(i==source):
            shortest[source] = 0 #graph[source][source]
        else:
            if(graph[source][i]==0):
                shortest[i] = inf
            else:
                shortest[i] = graph[source][i]
                if(shortest[i] < min_sel):
                    min_sel = shortest[i]
                    ind = i
                
    if(source==dest):
        return 0
    # Dijktra's in Play
    selected.append(ind) 
    while(ind!=dest):
        #print('ind',ind)
        for i in range(l):
            if i not in selected:
                if(graph[ind][i]!=0):
                    #Check if distance needs to be updated
                    if((graph[ind][i] + min_sel) < shortest[i]):
                        shortest[i] = graph[ind][i] + min_sel
        temp_min = 1000000
        #print('shortest:',shortest)
        #print('selected:',selected)
        
        for j in range(l):
            if j not in selected:
                if(shortest[j] < temp_min):
                    temp_min = shortest[j]
                    ind = j
        min_sel = temp_min
        selected.append(ind)
    
    return shortest[dest]
                            
#Finding odd degree vertices in graph

def get_odd(graph):
    degrees = [0 for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
                if(graph[i][j]!=0):
                    degrees[i]+=1
                
    #print(degrees)
    odds = [i for i in range(len(degrees)) if degrees[i]%2!=0]
    #print('odds are:',odds)
    return odds

#Function to generate unique pairs
def gen_pairs(odds):
    pairs = []
    for i in range(len(odds)-1):
        pairs.append([])
        for j in range(i+1,len(odds)):
            pairs[i].append([odds[i],odds[j]])
        
    #print('pairs are:',pairs)
    #print('\n')
    return pairs


#Final Compiled Function
def Chinese_Postman(graph):
    odds = get_odd(graph)
    if(len(odds)==0):
        return (sum_edges(graph), 'n/a')
    pairs = gen_pairs(odds)
    l = (len(pairs)+1)//2
    
    pairings_sum = []
    
    def get_pairs(pairs, done = [], final = []):
        
        if(pairs[0][0][0] not in done):
            done.append(pairs[0][0][0])
            
            for i in pairs[0]:
                f = final[:]
                val = done[:]
                if(i[1] not in val):
                    f.append(i)
                else:
                    continue
                
                if(len(f)==l):
                    pairings_sum.append(f)
                    return 
                else:
                    val.append(i[1])
                    get_pairs(pairs[1:],val, f)
                    
        else:
            get_pairs(pairs[1:], done, final)
            
    get_pairs(pairs)
    min_sums = {}
    for i in pairings_sum:
       #print(i)
        s = 0
        for j in range(len(i)):
            s += dijktra(graph, i[j][0], i[j][1])
        i_tup = [tuple(x) for x in i]
        i_tup = tuple(i_tup)
        min_sums[i_tup] =  s
    print(min_sums)
    chinese_dis = sum_edges(graph)
    added_dis = min(min_sums.values())
    chinese_dis = added_dis + sum_edges(graph)
    for key, value in min_sums.items():
        if added_dis == value:
            added_path = key
    if added_path == ():
        added_path = "n/a"
    return chinese_dis, added_path
def plot_graph(graph, added_path):
        for i in range(len(graph)):
            for x in range(i):
                if graph[i][x] != 0:
                    G.addEdge(x, i, length = graph[i][x])
        if added_path == 'n/a':
            return
        x = 0
        for i in range(len(added_path)):
            node_1 = added_path[i][0]
            node_2 = added_path[i][1]
            G.addEdge(node_1, len(graph) + x, length = dijktra(graph, node_1, node_2) / 2 )
            G.addEdge(node_2, len(graph) + x, length = dijktra(graph, node_1, node_2) / 2 )
            x+= 1
            
def Euler_Trail(graph, doubled):
    verticies = 8
    for i in range(len(graph)):
        verticies += 1
    g = Graph(verticies)
    for i in range(len(graph)):
        for x in range(i):
            if graph[i][x] != 0:
                g.addEdge(i, x)
    if doubled == 'n/a':
        g.printEulerTour()
    else:
        x = 0
        for i in range(len(doubled)):
            g.addEdge(doubled[i][1], len(graph) + x)
            g.addEdge(doubled[i][0], len(graph) + x)
            x += 1
        g.printEulerTour()
graph = graph2
distance, added_paths = Chinese_Postman(graph)
print('Chinese Postman Distance is:', distance)
print('Doubled paths are: ', added_paths)
plot_graph(graph, added_paths)
graphy = G.visualize()
Euler_Tour = Euler_Trail(graph, added_paths)
