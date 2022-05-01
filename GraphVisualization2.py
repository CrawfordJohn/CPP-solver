# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:42:51 2022

@author: John Crawford
"""


# First networkx library is imported 
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
   
  
# Defining a Class
class GraphVisualization:
   
    def __init__(self):
          
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
          
    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b, length = 0):
        temp = [a, b, {'length':length}]
        self.visual.append(temp)
          
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        #G.add_edge(0,1, length = 3.5)
        #G.add_edge(1,2, length = 10.5)
        #G.add_weighted_edges_from([(0, 1, 5.5), (1, 2, 0.5)])
        pos=nx.spring_layout(G)
        nx.draw_networkx(G, pos)
        
        labels = nx.get_edge_attributes(G,'length')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.show()
# Driver code


G = GraphVisualization()
G.visualize()
