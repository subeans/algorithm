# 시간제한 2초 메모리제한 4MB 
# 시간초과
# https://www.acmicpc.net/problem/2023

N = int(input())

def is_prime(number):
    if number == 2 :
        return True
    if number ==1 or number ==0 :
        return False
    if number % 2== 0:
        return False

    # 제곱근 범위로 줄일 수있다. 
    for n in range(3,number**0.5,2):
        if number%n ==0:
            return False
        
    return True

def make_num(num):
    if len(str(num))==N:
        print(num)
    else:
        for i in range(10):
            tmp_num=num*10+i
            if is_prime(tmp_num):
                make_num(tmp_num)

for i in range(1,10):
    if is_prime(i):
        make_num(i)