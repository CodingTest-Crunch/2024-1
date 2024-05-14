def solution(queries):
    arr = []
    answer = []
    for query in queries:
        if query[0] == "ADD":
            arr.append(int(query[1]))
            answer.append("")
            
        elif query[0] == "EXISTS":
            if int(query[1]) in arr:
                answer.append("true")
            else:
                answer.append("false")
                
        elif query[0] == "REMOVE":
            if int(query[1]) in arr:
                arr.remove(int(query[1]))
                answer.append("true")
            else:
                answer.append("false")
                
        elif query[0] == "GET_NEXT":
            arr.sort()
            for element in arr:
                if int(query[1]) < element:
                    answer.append(str(element))
                    break
                else:
                    if arr.index(element) == (len(arr)-1): #마지막 원소
                        answer.append("")
    return answer
