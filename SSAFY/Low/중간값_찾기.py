import math
import statistics

T = int(input().strip())

S = list(map(int, input().split()))

nums = sorted(S)

print(f'{nums[T//2]}')

#mid = T//2 + 1

#print(S)
#value = S[mid]
#print(value)
