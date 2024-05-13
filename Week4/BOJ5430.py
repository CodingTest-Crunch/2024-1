import sys
from collections import deque

# 시간 초과 솔루션 - 반복문 안에 또 reverse가 들어가면서 시간을 잡아먹음
"""
T = int(sys.stdin.readline())

p_list = []
n_list = []

for i in range(T) : 
    p_list.append(sys.stdin.readline().strip())
    num = int(sys.stdin.readline())
    
    temp = sys.stdin.readline().strip()
    if temp == "[]" : 
         n_list.append([]) 
         continue
     
    temp = temp.split(",")
    for i in range(num) : 
        if "[" in temp[i] : 
            temp[i]=temp[i].replace("[","")
        if "]" in temp[i] : 
            temp[i]=temp[i].replace("]","")
        temp[i]= int(temp[i])
    n_list.append(temp)        
    
 
def solution(str, calculate) : 
    arr = list(str)
    num_list= list(calculate)
    for cal in arr : 
        if cal == "R" : 
            num_list.reverse() 
        elif cal == "D" : 
            if len(num_list) == 0 : 
                print("error")
                return
            else : 
                num_list.pop(0)
    print(num_list)


for i in range(len(p_list)) : 
    solution(p_list[i],n_list[i] )
"""

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    nums = sys.stdin.readline().rstrip()[1:-1]
    if len(nums) > 0:
        nums = deque(nums.split(','))
    else:
        nums = deque()

    if p.count('D') > len(nums):
        print("error")
        continue

    r_flag = False
    for func in p:
        if func == 'R':
            r_flag = not r_flag
        elif func == 'D':
            if r_flag:
                nums.pop()
            else:
                nums.popleft()
    if r_flag:
        nums.reverse()

    result = ','.join(nums)
    print(f'[{result}]')