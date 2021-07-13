# 시간제한 2초 , 메모리제한 256 MB
# 시간 초과 

import sys
R, C = map(int, input().split())
map_ = [list(sys.stdin.readline().strip()) for _ in range(R)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

ans=1
# visited=[[0]*C]*R
check_alpha=[]

def solve(x,y,dist):
    global ans
    ans = max(ans,dist)
    # 상하 좌우 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 내의 인덱스인지 
        if 0<= nx < C and 0<= ny < R :
            # 지금까지 방문한 알파벳 아닌지 확인 
            if map_[ny][nx] not in check_alpha :
                dist+=1
                # print(map_[ny][nx] ," : ",dist,"(",ny,",",nx,")")
                check_alpha.append(map_[ny][nx])
                solve(nx,ny,dist)
                ################################# 경로의 최대값을 찾아야함 ###########################
                ans = max(ans,dist)
                ################################################################################
                check_alpha.pop()
                dist-=1


check_alpha.append(map_[0][0])
solve(0,0,ans)
print(ans)
