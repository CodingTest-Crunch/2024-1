import sys 

equation = sys.stdin.readline().strip()

ans = 0 
prev = 0 

if "-" not in equation : 
    nums = list(map(int,equation.split("+")))
    sum = 0
    for num in nums : 
        sum += num 
    ans += sum
    
i = 0 

while i < len(equation) : 
    if equation[i] == "-" : 
        if "+" in equation[prev : i] : 
            nums = list(map(int,equation[prev:i].split("+")))
            print(nums)
            s = 0 
            for num in nums : 
                s += num 
            ans += s
        else : 
            ans += int(equation[prev:i])
        print("ans" , ans)
        
        sum = 0 
        j = i + 1
        while j < len(equation) : 
            if equation[j] == "-" : 
                break 
            j += 1
        if "+" in equation[i+1:j] : 
            nums = list(map(int,equation[i+1:j].split("+")))
            print(nums)
            sum = 0 
            for num in nums : 
                sum += num 
            ans -= sum 
        else : 
            ans -= int(equation[i+1:j])
            print("gg", ans, equation[i+1:j])
        prev = j
        i = prev
    else : 
        i += 1
    
print(ans)
            