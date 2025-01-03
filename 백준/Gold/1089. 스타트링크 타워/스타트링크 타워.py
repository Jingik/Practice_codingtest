import sys
#,
input = sys.stdin.readline
n = int(input())
g = [list(map(str, list(input().strip()))) for _ in range(5)]
numOfNum = [0 for _ in range(n)] # 해당 자릿수에 나올 수 있는 숫자 개수
sumOfNum = [0 for _ in range(n)] # 해당 자릿수에 나올 수 있는 숫자들의 합
totalNum = 1 # 나올 수 있는 경우의 수
ans = 0 # .정답.

# 숫자 별 '.'이 들어가 있는 좌표를 해시에 저장
numHt = { 0 : [[1, 1], [2, 1], [3, 1]],
          1 : [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1], [3, 0], [3, 1], [4, 0], [4, 1]],
          2 : [[1, 0], [1, 1], [3, 1], [3, 2]],
          3 : [[1, 0], [1, 1], [3, 0], [3, 1]],
          4 : [[0, 1], [1, 1], [3, 0], [3, 1], [4, 0], [4, 1]],
          5 : [[1, 1], [1, 2], [3, 0], [3, 1]],
          6 : [[1, 1], [1, 2], [3, 1]],
          7 : [[1, 0], [1, 1], [2, 0], [2, 1], [3, 0], [3, 1], [4, 0], [4, 1]],
          8 : [[1, 1], [3, 1]],
          9 : [[1, 1], [3, 1], [3, 0]]
}

nj = 0 # 맵을 오른쪽으로 4씩 옮기기 위한 새로운 j값
for idx in range(n):
    for num in range(10):
        numValueArr = numHt[num] # 숫자별 모든 '.'의 좌표
        cnt = 0 
        for i, j in numValueArr:
            j = nj + j
            # 그래프상의 '.' 좌표와 한 숫자마다의 '.' 좌표가 일치하면 cnt를 1증가
            if g[i][j] == '.':
                cnt += 1
            # 그 개수가 숫자의 개수와 일치할 때
            if cnt == len(numValueArr):
                sumOfNum[idx] += num * (10 ** (n - idx - 1)) # num(0 ~ 9 중 하나) * (해당 자릿수가 가지는 0의 개수) 를 해당 자릿수 번째에 넣기
                numOfNum[idx] += 1 # 해당 자릿수의 개수를 1증가
    nj = nj + 4

for i in range(n):
    numSum = 1
    for j in range(n):
        if i != j:
            numSum *= numOfNum[j] # 해당 자릿수가 나오는 개수
        if i == 0:
            totalNum *= numOfNum[j] # 나올 수 있는 총 숫자 개수
    ans += sumOfNum[i] * numSum # 해당 자릿수 총합 * 해당 자릿수가 나오는 개수

# 아무 경우도 나올 수 없는 예외 처리
if totalNum == 0:
    print(-1)
    exit(0)
print(ans / totalNum)
