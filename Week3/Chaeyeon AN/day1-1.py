n, m, k = map(int, input().split())
data = list(map(int, input().split()))

result = 0

data.sort()

first_max = data[n-1]
second_max = data[n-2]

result = first_max * k * (m // k) + second_max * (m % k)

print(result)
