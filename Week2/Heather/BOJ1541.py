import sys 

equation = sys.stdin.readline().strip()

arr = list(equation.split("-"))

sum = 0
for i in range(len(arr)): 
    s= 0 
    if "+" in arr[i] : 
        temp = list(map(int, arr[i].split("+")))
        for num in temp : 
            s += num
    else : 
        s = int(arr[i])
            
    if i == 0 : 
        sum += s
    else: 
        sum -= s

print(sum)