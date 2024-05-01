import sys 

# 현재 100번

target = int(sys.stdin.readline())
ans = abs(100 - target)
M = int(sys.stdin.readline())

if M : 
    broken = list(map(str, sys.stdin.readline().split()))
else:
    broken = []
#만약에 +,-로만 이동 가능할 경우 이게 최솟값!

# 자릿수만큼 숫자 버튼 누르는 횟수 + +/- 횟수 
# 만약에 N이 500000이면 100에서 +만 눌러서 오는 것보다 600000에서 오는 게 더 가까울 수 있다 
# 따라서 500000을 100부터 ++만으로 오는게 499900이니까 
# 그것보다 적게 걸리는 범위 내에서 500000보다 큰 수까지 돌려줘야한다 
# 따라서 
for num in range(999900) : 
    for N in str(num) : 
        if N in broken : 
            break 
    else : 
        ans = min(ans, len(str(num)) + abs(num-target))

print(ans)

