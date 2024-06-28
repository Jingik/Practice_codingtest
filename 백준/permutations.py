def permutations(arr, n):
    result = []
    def backtrack(start):
        if start == n - 1:
            result.append(arr[:])
            return
        for i in range(start, n):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]
    backtrack(0)
    return result

List = [1, 2, 3, 4]
print(permutations(List, 3))