import sys

n = int(sys.stdin.readline())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))
numbers.sort(reverse=True)

for i in numbers:
    print(i)
