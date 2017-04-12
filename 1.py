from collections import *
import pdb
import socket
import re, time
from threading import Thread
from random import randint
import os,re,socket,time,hashlib
from datetime import datetime
from collections import *


class Server(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        port = 60000
        s = socket.socket()
        host = ""
        s.bind((host, port))
        s.listen(5)
        print 'Server listening....'
        # relax(0)
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

        # print len(graph)
        # for i in graph:
        # d, p = bellman_ford(graph, i)
        d = defaultdict(dict) # Stands for destination
        # p = {} # Stands for predecessor
        for node in graph:
            for Node in graph:
                if node != Node:
                    d[node][Node] = float('Inf') # We start admiting that the rest of nodes are very very far
                else: d[node][Node] = 0
        # d = initialize(graph, source)
        for i in range(len(graph)-1): #Run this until is converges
            for u in graph:
                conn, addr = s.accept()
                time.sleep(0.3);
                print "lol"
                tosend=""
                for v in graph: #For each neighbour of u
                    tosend = tosend + str(v) + ' ' + str(d[u][v]) + "\n";
                    # relax(u, v, graph, d, p) #Lets relax it
                forwd_table_u = str(u) + ' ' + tosend
                print "table sent"
                conn.send(forwd_table_u)
                conn.close()

        for u in graph:
            for v in graph[u]:
                assert d[v] <= d[u] + graph[u][v]

        # def initialize(graph, source):
                    # p[node][Node] = None
            # d[source] = 0 # For the source we know how to reach
            # return d

        # def bellman_ford(graph, source):
        
            # return d, p


        # def test(graph):
class Receiver(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):

        # def relax(flag):
        # forwarding table
        # node + forwarding table of neighbour
        # d[neighbour] is the value of distance and this is called for all neighbours
        # recv(1024)
        s = socket.socket()
        host = ""
        port = 60000
        s.connect((host, port))
        # s.send("Hello server!")
        while True:
            print "relax called";

                # return
            # if flag==1:
            print "waiting to rec"
            data = s.recv(1024)
            print data;
        s.close()
        # if d[neighbour] > d[node] + graph[node][neighbour]:
        #     # update
        #     d[neighbour] = d[node] + graph[node][neighbour]
        #     p[neighbour] = node



if __name__ == '__main__': 

    # print graph
    rec=Receiver()
    ser=Server()
    # myThreadOb1 = MyThread(4)
    # myThreadOb1.setName('Thread 1')

    # myThreadOb2 = MyThread(4)
    # myThreadOb2.setName('Thread 2')

    # Start running the threads!
    ser.start()
    time.sleep(3)
    rec.start()

    # Wait for the threads to finish...
    ser.join()
    rec.join()
