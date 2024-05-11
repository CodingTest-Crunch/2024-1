import sys 

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

dp = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]

for i in range(1, len(A)+1): 
    for j in range(1,len(B)+1): 
        # 만약 같으면 그 전 인덱스의 값에 +1 
        if A[i-1] == B[j-1] : 
            dp[i][j] = dp[i-1][j-1] + 1
        # 만약 같지 않으면 
        # AB GBC를 생각해보자 
        # B와 C가 같지 않으니 dp[2][3]은
        # A, GBC / AB, GB의 LCS 길이 중 큰 값이 들어가는 것 
        # 따라서 i-1, j / i, j-1 케이스로 나눌 수 있다 
        else : 
            if dp[i-1][j] >= dp[i][j-1] : 
                dp[i][j] = dp[i-1][j]
            else : 
                dp[i][j] = dp[i][j-1]

print(dp[len(A)][len(B)])