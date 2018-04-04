import sys

class Node:
    def __init__(self, _v, _w):
        self.v = _v
        self.w = _w

inputData = sys.stdin.readline()
V, E = map(int, inputData[0].split())
K = int(inputData[1])
graph = {}

for i in range(2, 2 + E):
    u, v, w = map(int, inputData[i].split())
    try:
        graph[u].append(Node(v,w))
    except KeyError:
        graph[u] = [Node(v,w)]
        
path = [None for _ in range(V+1)]
path[K] = 0
queue = [K]

while queue:
    _u = queue.pop(0)
    _w = path[_u]
    try:
        for node in graph[_u]:
            if path[node.v] == None or path[node.v] > _w + node.w:
                path[node.v] = _w + node.w
                queue.append(node.v)
    except KeyError:
        continue 
        
for i in range(1, V+1):
    if path[i] == None:
        print('INF')
    else:
        print(path[i])



n = input()