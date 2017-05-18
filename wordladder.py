from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue
import datetime
from dataset import *


g = Graph()
def make_graph():

    for word in data.keys():
        for i in data[word]:

            g.addEdge(word,i)
            g.getVertex(i).setColor('white')
            g.getVertex(word).setColor('white')
    return g

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())
  

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')
  nbr.setColor('gray')
  nbr.setDistance(currentVert.getDistance() + 1)


while(1):
    wordgraph = make_graph()
    a = input("enter first word : ")
    b = input("enter end word : ")

    print(datetime.datetime.now())

    bfs(wordgraph ,wordgraph.getVertex(b))
    traverse(wordgraph.getVertex(a))

    print(datetime.datetime.now());

   
