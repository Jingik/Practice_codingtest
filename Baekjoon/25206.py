import sys

Rank = {'A+': '4.5', 'A0': '4.0', 'B+': '3.5', 'B0': '3.0', 'C+': '2.5',
        'C0': '2.0', 'D+': '1.5', 'D0': '1.0', 'F': '0.0'}

result = 0
n = 0

for i in range(20):
    name, number, rank = map(str, input().split())
    if rank == 'P':
        continue
    else :
        trans_number = float(number)
        n = n + trans_number
        rank_number = float(Rank.get(rank))
        result = result + (trans_number * rank_number)

final_result = result / n

print(final_result)