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
                
    return answer
