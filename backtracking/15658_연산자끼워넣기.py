# 시간제한 2초 , 512 MB 메모리 제한 
# 정답 
# https://www.acmicpc.net/problem/15658

N = int(input())
a = list(map(int,input().split()))
cnt = list(map(int,input().split()))

max_ans = -1000000000
min_ans = 1000000000

def calc(idx, ans):  
    global max_ans , min_ans  
    if idx == N:
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        return
    
    if cnt[0] > 0:
        cnt[0] -= 1
        calc(idx+1, ans+a[idx])
        cnt[0] += 1
    if cnt[1] > 0:
        cnt[1] -= 1
        calc(idx+1, ans-a[idx])
        cnt[1] += 1
    if cnt[2] > 0:
        cnt[2] -= 1
        calc(idx+1, ans*a[idx])
        cnt[2] += 1
    if cnt[3] > 0:
        cnt[3] -= 1
        calc(idx+1, int(ans/a[idx]))
        cnt[3] += 1
        
calc(1,a[0])
print(max_ans)
print(min_ans)