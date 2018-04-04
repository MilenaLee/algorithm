N, M, V = map(int, input().split())
visit = {}
load = {}

for i in range(M):
    fromN, toN = map(int, input().split())
    visit[fromN] = 0
    visit[toN] = 0 
    try:
        load[fromN].append(toN)
    except KeyError:
        load[fromN] = [toN]
    
    try:
        load[toN].append(fromN)
    except KeyError:
        load[toN] = [fromN]
        
for a in load:
    load[a].sort()
    
dfsPath = []
def DFS(startV):
    dfsPath.append(startV)
    visit[startV]=1
    for toN in load.get(startV):
        if visit.get(toN) == 0:
            DFS(toN)

bfsPath = [V]
q = [V]
def BFS():
    while q:
        v = q.pop(0)
        for toN in load.get(v):
            if visit.get(toN)==0:
                bfsPath.append(toN)
                visit[toN]=1
                q.append(toN)
           
DFS(V)

for i in visit.keys():
    visit[i]=0

visit[V] = 1
BFS()

result = ''
for i in dfsPath:
    result += str(i)+' '
    
print(result[:len(result)-1])

result = ''
for i in bfsPath:
    result += str(i)+' '
print(result[:len(result)-1])