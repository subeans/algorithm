# 시간제한 2초 , 메모리제한 512B
# 2<=N<=11 , 1<= Ai <=100 , N-1<= 연산자 총 개수 <=4N

l = int(input())
num = []
for i in range(l):
    n = int(input())
    num.append(n)

# plus , minus , multiple , divide   
pmmd = []
for i in range(4):
    s = int(input())
    pmmd.append(s)

################################################################### 입력 받기 
def compare(n1,n2):
    calc=[]
    add = n1+n2
    minus = n1 - n2 
    mul = n1 * n2
    if n1 < 0 :
        div = -(-n1 // n2)
    else: 
        div = n1 // n2
    calc.append(add)
    calc.append(minus)
    calc.append(mul)
    calc.append(div)
    return calc

max_value = 0
min_value = 0
number = num[0]


for i in range(1,l):
    next_number = num[i]
    calc= compare(number,next_number)
    
    # 계산 결과가 최대값인 연산자 인덱스 
    max_op = calc.index(max(calc))
    if pmmd[max_op] <= 0 :
        calc.pop(max_op)
        max_op = calc.index(max(calc))

    calc_max = max(calc)

    calc_min = min(calc)
    min_op = calc.index(min(calc))
    
