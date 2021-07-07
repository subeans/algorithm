# 시간제한 1초 , 메모리제한 512MB 
# 정답 
# https://www.acmicpc.net/problem/15652

N, M = map(int, input().split())
out = []

def solve(length, idx, N, M):
    if length == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        out.append(i+1)
        solve(length+1, i, N, M)
        out.pop()

solve(0, 0, N, M)