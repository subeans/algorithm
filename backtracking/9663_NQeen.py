# 시간제한 10초 ,128 MB 
# 시간초과 
# https://www.acmicpc.net/problem/9663
import sys
input = sys.stdin.readline

N = int(input())
D = [[0]*N for _ in range(N)]
ck_col = [0] * N
ck_dg = [0] * (2*N-1)
ck_dg2 = [0] * (2*N-1)

def ck(row, col):
    if ck_col[col] == 1:
        return False 
    if ck_dg[row + col] == 1:
        return False
    if ck_dg2[row - col + N-1] == 1:
        return False
    return True

def nqueen(row):
    if row == N:
        return 1
    result = 0
    for col in range(N):
        if ck(row, col):
            D[row][col] = 1
            ck_col[col] = 1
            ck_dg[row + col] = 1
            ck_dg2[row - col + N-1] = 1

            result += nqueen(row + 1)
            
            D[row][col] = 0
            ck_col[col] = 0
            ck_dg[row + col] = 0
            ck_dg2[row - col + N-1] = 0
    return result


print(nqueen(0))