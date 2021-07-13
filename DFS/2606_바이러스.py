# 시간초과 3초 , 메모리제한 512 MB 
# 정답 

N = int(input())
M = int(input())

adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0


for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


def dfs(vertex):
    global count
    visited[vertex]=True
    for v in adj[vertex]:
        if visited[v]==False:
            count+=1
            dfs(v)
    


dfs(1)
print(count)