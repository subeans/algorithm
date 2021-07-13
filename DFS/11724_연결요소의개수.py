# 시간초과 3초 , 메모리제한 512 MB 
# 시간초과 

import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0


for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


def dfs(vertex):
    visited[vertex]=True
    for v in adj[vertex]:
        if visited[v]==False:
            dfs(v)
    return


for i in range(1,N+1):
    if visited[i] == 0:
        count+=1
        dfs(i)

print(count)