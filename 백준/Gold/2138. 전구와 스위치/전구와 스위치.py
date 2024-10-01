def toggle(arr, i, N):
    # i 번째 스위치를 눌렀을 때 전구 상태를 토글
    if i > 0:
        arr[i - 1] = '0' if arr[i - 1] == '1' else '1'
    arr[i] = '0' if arr[i] == '1' else '1'
    if i < N - 1:
        arr[i + 1] = '0' if arr[i + 1] == '1' else '1'

def solve(N, current, target):
    # 첫 번째 스위치를 누르지 않는 경우와 누르는 경우를 각각 처리
    arr1 = current[:]
    arr2 = current[:]
    
    # 1. 첫 번째 스위치를 누르지 않는 경우
    count1 = 0
    for i in range(1, N):
        if arr1[i - 1] != target[i - 1]:
            toggle(arr1, i, N)
            count1 += 1

    # 2. 첫 번째 스위치를 누르는 경우
    toggle(arr2, 0, N)
    count2 = 1
    for i in range(1, N):
        if arr2[i - 1] != target[i - 1]:
            toggle(arr2, i, N)
            count2 += 1

    # 가능한지 확인하고 최소값 반환
    if arr1 == target and arr2 == target:
        return min(count1, count2)
    elif arr1 == target:
        return count1
    elif arr2 == target:
        return count2
    else:
        return -1

# 입력 처리
N = int(input())
current = list(input().strip())
target = list(input().strip())

# 결과 출력
print(solve(N, current, target))
