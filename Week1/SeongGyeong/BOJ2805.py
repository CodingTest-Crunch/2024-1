import sys 

N, M = map(int, sys.stdin.readline().split(' '))
woods = list(map(int, sys.stdin.readline().split(' ')))

start, end = 0, max(woods)
mid = 0 
ans = 0 

while start<=end : 
    mid = (start + end) // 2
    rest = 0 
    
    for wood in woods : 
        if wood - mid > 0 : 
            rest += wood - mid 
        if rest > M : 
            break
    # 남는 나무 길이의 총합이 M임을 만족하는 톱날의 높이가 여러개인 경우를 생각해보면, 
    # 높이를 점점 높혀가면서 조건을 만족하는 높날의 높이가 최대인 경우까지 계속 진행해나가야한다.
    if rest>=M : 
        start = mid + 1
    else : 
        end = mid - 1 
        
# 결국 마지막에는 start가 end보다 1 많은 상태로 return 되게 된다. 
# 그 상태에서 (start+end)//2 를 하면 end가 항상 나오게 된다. 
print(end)

