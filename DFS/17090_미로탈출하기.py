# 시간제한 1초 , 메모리제한 512 MB
# 시간초과 

import sys
sys.setrecursionlimit(10**9)

N, M = map(int, sys.stdin.readline().rstrip().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

count = 0

def dfs(row,col):
    global count
    if row >= N or col >= M or row < 0 or col < 0 :
        count+=1
        return 

    elif visited[row][col]==False:
        visited[row][col]=True

        if board[row][col]=='U':
            dfs(row-1,col)
            visited[row][col]=False
        elif board[row][col]=='R':
            dfs(row,col+1)
            visited[row][col]=False

        elif board[row][col]=='D':
            dfs(row+1,col)
            visited[row][col]=False

        elif board[row][col]=='L':
            dfs(row,col-1)
            visited[row][col]=False

    else:
        return

for r in range(N):
    for c in range(M):   
        dfs(r,c)

print(count)