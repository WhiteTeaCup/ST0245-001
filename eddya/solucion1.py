import pandas as pd
class graph:
    def init(self, ari, n):
        self.adjList = [None] * n
        for i in range(n):
            self.adjList[i] = []
        for (origin, destination, lenght) in ari:
            self.adjList[origin].append((destination, lenght))

dataf = pd.read_csv("data_noblankfix.csv")

dataf.drop("geometry", inplace=True, axis=1)
dataf.drop("node", inplace=True, axis=1)
dataf.drop("null", inplace=True, axis=1)
dataf.drop("weights", inplace=True, axis=1)
dataf.drop("edges", inplace=True, axis=1)
dataf.drop("harassmentrisk", inplace=True, axis=1)

graph(dataf, 68750)

def BFSbusc(graph, sta, end):
    visited=[]
    deq = [[sta]]
    
    while deq:
        path = deq.pop(0)
        node = path[-1]
        if node not in visited:
            adj = graph[node]
            for a in adj:
                newpath = list(path)
                newpath.append(a)
                deq.append(newpath)
                if a == end:
                    print("el camino mas corto es ", *newpath)
                    return
            visited.append(node)
    print("no hay camino disponible")
    return

nomcal = input(str())
destcal = input(str())
tempor = dataf.origin[nomcal]
tempdes = dataf.origin[destcal]

BFSbusc(graph, tempor, tempdes)