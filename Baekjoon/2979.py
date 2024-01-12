import sys

def input():
    return sys.stdin.readline().strip()

arr = [0]*100 
A,B,C = map(int, input().split())

cal3 = 0
cal2 = 0
cal1 = 0

for _ in range(3):
	First, End = map(int, input().split())
	for point in range(First, End):
		arr[point] += 1

for i in range(100):
	if arr[i] == 3:
		cal3 += 1
	elif arr[i] == 2:
		cal2 += 1
	elif arr[i] == 1:
		cal1 += 1

answer = (cal3*C*3)+(cal2*B*2)+(cal1*A*1)
print(answer)