import sys
input = sys.stdin.readline

# 입력
N = int(input())
liquids = list(map(int, input().split()))

# 용액 배열을 정렬
liquids.sort()

# 결과 저장용 변수들
closest_sum = float('inf')  # 가장 0에 가까운 합을 저장
result = []  # 가장 0에 가까운 세 용액을 저장

# 첫 번째 용액을 고정하고 나머지 두 용액을 투 포인터로 찾는다
for i in range(N - 2):
    left = i + 1  # 두 번째 용액의 시작 포인터
    right = N - 1  # 세 번째 용액의 시작 포인터
    
    while left < right:
        current_sum = liquids[i] + liquids[left] + liquids[right]
        
        # 0에 더 가까운 값을 찾으면 업데이트
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            result = [liquids[i], liquids[left], liquids[right]]
        
        # 현재 합이 0보다 크다면, 더 작은 값으로 가기 위해 right를 줄임
        if current_sum > 0:
            right -= 1
        # 현재 합이 0보다 작다면, 더 큰 값으로 가기 위해 left를 늘림
        elif current_sum < 0:
            left += 1
        # 정확히 0이면 바로 종료
        else:
            print(liquids[i], liquids[left], liquids[right])
            sys.exit()

# 결과 출력 (오름차순으로 정렬)
result.sort()
print(*result)
