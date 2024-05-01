# https://school.programmers.co.kr/learn/courses/30/lessons/42862#

def solution(n, lost, reserve):
    
    set_reserve = list(set(reserve) - set(lost))
    set_lost = list(set(lost) - set(reserve))
    
    answer = n - len(set_lost)
    
    for student in  set_reserve:
        for i in range(len(set_lost)):
            if(set_lost[i]==student-1 or set_lost[i]==student+1):
                answer+=1
                set_lost[i]=-1
                break

    return answer