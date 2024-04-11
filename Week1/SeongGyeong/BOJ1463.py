import sys 

N = int(sys.stdin.readline())
dp = [0] * (10**6+1)

if N == 2 or N == 3: 
    print(1)
else : 
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4,N+1) : 
        # 3으로 나눠질 때 
        if i % 2 == 0 and i % 3 == 0 : 
            dp[i] = min(dp[i-1] + 1, dp[i//2] + 1, dp[i//3] + 1)
        elif i % 2 == 0 : 
            dp[i] = min(dp[i-1] + 1, dp[i//2] + 1)
        elif i % 3 == 0 : 
            dp[i] = min(dp[i-1] + 1, dp[i//3] + 1)
        else : 
            dp[i] = dp[i-1] + 1
    print(dp[N])