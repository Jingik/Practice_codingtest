def combinations(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for i in combinations(rest_arr, n-1):
            result.append([elem] + i)
    return result

List = [1, 2, 3, 4]
print(combinations(List, 3))