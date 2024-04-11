import sys
input = sys.stdin.readline

rm_num = int(input()) #시험장 개수
st_num= list(map(int, input().split())) 

n, m = map(int, input().split()) #n: 총감독관 감시 응시자수, m: 부감독관 감시 응시자수
left = 0 #시험장마다 남은 응시자수 저장 변수
count = 0 #필요 감독관 수 세는 변수

for i in range(rm_num):
    left = st_num[i] - n #일단 총감독관 1명 배치
    count += 1
    if (left > 0): #주의: 파이썬은 음수를 포함한 나눗셈이 가능!!
        count += (left // m)
        if (left % m > 0):
            count += 1
    
print(count)

