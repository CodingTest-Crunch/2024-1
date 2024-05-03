# https://school.programmers.co.kr/learn/courses/30/lessons/42860?language=python3#

def solution(name):
    
    answer = 0
    length = len(name)
    move = length - 1 # 오른쪽으로만 이동하는 기본값 설정
    
    for idx in range(length):
        # 위/아래로 조이스틱을 움직여 알파벳을 맞추는 최소 횟수를 더함
        if(ord(name[idx]) - ord('A') <= 13):
            answer += (ord(name[idx]) - ord('A'))
        else:
            answer += (26 - (ord(name[idx]) - ord('A')))
        
        # 현재 위치에서 다음에 A가 아닌 문자가 나타나기까지의 거리를 계산
        next_idx = idx + 1
        while next_idx < length and name[next_idx] == 'A':
            next_idx += 1
        
        # 시작에서 현재 위치까지 오는 거리와, 다음 A가 아닌 문자까지 다시 돌아가는 거리 중 최소값을 구하여 이동 거리 계산
        move = min(move, idx + idx + length - next_idx, 2*idx + length - next_idx, idx + 2*(length - next_idx))
    
    answer += move
    
    return answer