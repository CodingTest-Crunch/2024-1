# https://www.acmicpc.net/problem/11399

x= int(input('people: '))
time_array=[]
sum=0

for _ in range(x):
   time_array.append(int(input('time: ')))

time_array=sorted(time_array)

for time in range(len(time_array)):
   sum=sum+time_array[time]*(len(time_array)-time)

print(sum)