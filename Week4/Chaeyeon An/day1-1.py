# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3

def solution(numbers, target):
    count = 0

    def dfs(index, sum):
        nonlocal count 
        if index == len(numbers):
            if sum == target:
                count += 1
            return

        dfs(index + 1, sum + numbers[index])
        dfs(index + 1, sum - numbers[index])

    dfs(0, 0)

    return count
