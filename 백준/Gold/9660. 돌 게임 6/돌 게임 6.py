import sys
input = sys.stdin.readline

N = int(input())
x = N % 7
Test = [1, 3, 4, 5, 6]
# 1 3 4 5 6 = SK or 0 2 = CY
if  x in Test:
    print('SK')
else:
    print('CY')