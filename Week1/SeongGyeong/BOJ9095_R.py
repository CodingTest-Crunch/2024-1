import sys 

T = int(sys.stdin.readline())
nums = []
for _ in range(T) : 
    nums.append(int(sys.stdin.readline()))
dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for num in nums : 
    if num <= 4 : 
        print(dp[num])
    else : 
        for i in range(5, num+1) : 
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[num])

