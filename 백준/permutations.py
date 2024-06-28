def permutations(arr, k):
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(0, path + arr[:i] + arr[i+1:])  # 다음 단계로 이동하면서 사용한 원소 제외
            path.pop()
    
    backtrack(0, [])
    return result

List = [1, 2, 3, 4]
print(permutations(List, 3))
