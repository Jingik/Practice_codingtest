N = int(input())  # 건물의 수 입력

heights = [0] * 1001  # 각 위치의 건물 높이를 저장할 리스트
max_h = 0  # 가장 높은 건물 높이
max_i = 0  # 가장 높은 건물의 위치

# 건물 정보 입력 및 처리
for _ in range(N):
    l, h = map(int, input().split())
    heights[l] = h  # 건물 위치에 해당하는 높이 저장
    if max_h < h:
        max_h = h
        max_i = l

# 좌측에서부터 최고 높이까지의 면적 계산
total_area = 0
high_area = 0
for i in range(max_i + 1):
    high_area = max(high_area, heights[i])
    total_area += high_area

# 우측에서부터 최고 높이까지의 면적 계산
high_area = 0
for i in range(1000, max_i, -1):
    high_area = max(high_area, heights[i])
    total_area += high_area

print(total_area)  # 총 면적 출력