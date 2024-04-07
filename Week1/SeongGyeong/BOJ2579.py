import sys

# 계단이 하나만 주어지는 경우 인덱스 에러가 나니까 
# 배열은 일단 최대 인풋 크기만큼 0으로 채워놓기!
N = int(sys.stdin.readline())
stairs = []
dp= [0] * 500

for i in range(N) : 
    num = int(sys.stdin.readline())
    stairs.append(num)

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3, N) :
    dp[i] = max(dp[i-2] + stairs[i], stairs[i-1] + dp[i-3] + stairs[i])

print(dp[N-1])