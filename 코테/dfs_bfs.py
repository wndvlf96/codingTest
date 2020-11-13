from collections import deque

ex_grp = [
    [],             #0
    [2,3,8],        #1
    [1,7],          #2
    [1,4,5],        #3
    [3,5],          #4
    [3,4],          #5
    [7],            #6
    [2,6,8],        #7
    [1,7]           #8
    ]


def dfs(graph, v ,visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        print(x, end= ' ')
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited1 = [False,False,False,False,False,False,False,False,False]
visited2 = [False,False,False,False,False,False,False,False,False]

dfs(ex_grp, 1 ,visited1)
print()
bfs(ex_grp, 1 ,visited2)
print()
prob_graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
    ]

def dfs_icecream(x,y,prob):
    if x < 0 or y <0 or x>= (len(prob)) or y>= (len(prob[0])):
        return False
    if prob[x][y] == 0:
        prob[x][y] = 1
        dfs_icecream(x-1,y,prob)
        dfs_icecream(x,y-1,prob)
        dfs_icecream(x+1,y,prob)
        dfs_icecream(x,y+1,prob)
        return True
    return False

def icecream(prob):
    ans = 0
    for i in range(len(prob)):
        for j in range(len(prob[i])):
            if dfs_icecream(i,j,prob) == True:
                ans = ans +1
    return ans

print(icecream(prob_graph))