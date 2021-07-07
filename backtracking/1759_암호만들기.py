# 시간제한 2초 , 메모리제한 128MB 
# 정답 
# https://www.acmicpc.net/problem/1759

L, C = map(int, input().split())
alpha = list(map(str,input().split()))
alpha.sort()

out = []
all_out = []

def solve(length, idx, L, C):
    if length == L:
        all_out.append(''.join(map(str, out)))
        return
    for i in range(idx, C):
        out.append(alpha[i])
        solve(length+1, i+1, L, C)
        out.pop()

def password(list_check):
    for i in list_check:
        cons = 0
        vow = 0
        for j in i:
            if j in 'aeiou':
                cons += 1
            else:
                vow += 1
        if cons >= 1 and vow >= 2:
            print(i)
    return

solve(0, 0, L, C)
password(all_out)