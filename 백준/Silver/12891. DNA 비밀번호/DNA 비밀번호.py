import sys
input = sys.stdin.readline
Dict = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
Len, Sp_len = map(int, input().split())
Word = input()
A, C, G, T = map(int, input().split())
for ex in Word[:Sp_len]:
    if ex in 'ACGT':
        Dict[ex] += 1
left = 0
right = Sp_len - 1
Count = 0
while 1:
    if Dict['A'] >= A and Dict['C'] >= C and  Dict['G'] >= G and  Dict['T'] >= T:
        Count += 1
    Dict[Word[left]] -= 1
    left += 1
    right += 1
    if right == Len:
        break
    Dict[Word[right]] += 1


print(Count)