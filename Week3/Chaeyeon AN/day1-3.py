m,n=map(int,input().split())

result=0

for i in range(m):
    data=list(map(int, input().split()))
    minimum=min(data)
    result=max(result, minimum)

print(result)
    