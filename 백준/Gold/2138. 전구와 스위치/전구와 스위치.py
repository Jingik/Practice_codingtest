def toggle(arr, i, N):
    if i > 0:
        arr[i - 1] = '0' if arr[i - 1] == '1' else '1'
    arr[i] = '0' if arr[i] == '1' else '1'
    if i < N - 1:
        arr[i + 1] = '0' if arr[i + 1] == '1' else '1'

def solve(N, current, target):
    arr1 = current[:]
    arr2 = current[:]
    count1 = 0
    for i in range(1, N):
        if arr1[i - 1] != target[i - 1]:
            toggle(arr1, i, N)
            count1 += 1

    toggle(arr2, 0, N)
    count2 = 1
    for i in range(1, N):
        if arr2[i - 1] != target[i - 1]:
            toggle(arr2, i, N)
            count2 += 1

    if arr1 == target and arr2 == target:
        return min(count1, count2)
    elif arr1 == target:
        return count1
    elif arr2 == target:
        return count2
    else:
        return -1


N = int(input())
current = list(input().strip())
target = list(input().strip())

print(solve(N, current, target))
