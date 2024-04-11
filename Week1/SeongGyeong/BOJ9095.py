import sys 

T = int(sys.stdin.readline())
cases = [int(sys.stdin.readline()) for _ in range(T)]

dp = [0] * 12

dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7 
dp[5] = 13

for case in cases : 
    if case <= 5 : 
        print(dp[case])
    else : 
        for i in range(6, case+1) : 
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3] 
        print(dp[case])