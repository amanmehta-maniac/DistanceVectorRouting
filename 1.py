from collections import *
import pdb

def initialize(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    # forwarding table
    # node + forwarding table of neighbour
    # d[neighbour] is the value of distance and this is called for all neighbours.
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # update
        d[neighbour] = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            for v in graph[u]: #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it

    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p


def test(graph):
    print len(graph)
    for i in graph:
        d, p = bellman_ford(graph, i)
        print len(graph)-1,
        for j in d:
            if j!=i:
                print j,d[j],
        print

if __name__ == '__main__': 
    graph, i = defaultdict(dict), 0
    with open('test') as f:
        lines = f.readlines()
        for i in range(1+int(lines[0])):
            gf = lines[i].split()
            if i != 0:
                k=1
                for l in range(int(gf[0])):
                    graph[i][int(gf[k])] = int(gf[k+1])
                    k=k+2
    # print graph
    test(graph)