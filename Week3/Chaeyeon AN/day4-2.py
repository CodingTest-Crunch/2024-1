# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3

import math

def solution(progresses, speeds):
    answer = []
    temp=[]
    
    for i in range (len(speeds)):
        progresses[i]=math.ceil((100-progresses[i])/speeds[i])
    
    for i in range (len(progresses)):
        if(len(temp)== 0 or progresses[i] <= temp[0] ):
            temp.append(progresses[i])
        else:
            answer.append(len(temp))
            temp=[]
            temp.append(progresses[i])
        if(i == len(progresses)-1):
            answer.append(len(temp))
    
    return answer