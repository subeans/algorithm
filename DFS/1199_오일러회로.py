# 시간제한 2초 , 메모리제한 256 MB
# 시간초과 
import sys
sys.setrecursionlimit(10**9)

N= int(input())
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
# visited = [False] * N

def dfs(v):
    print(v+1)
    for i in range(N):
        if board[v][i]>0 :
            board[v][i]-=1
            board[i][v]-=1
            dfs(i)

# 오일러 회로를 할 수 없다면 -1 출력 방법 
# 오일러 회로 ( undirected graph ) 모든 정점의 차수가 짝수이다. 
check=True
for i in range(N):
    if sum(board[i])%2 != 0:
        check=False
        break

if check :
    dfs(0)
else:
    print(-1)