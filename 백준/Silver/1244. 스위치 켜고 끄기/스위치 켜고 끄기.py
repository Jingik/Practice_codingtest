def isvaild(x, y, N):
    if 0 <= x and x < N and 0 <= y and y < N:
        return True
    else:
        return False
def list_chunk(list, n):
    return[list[i:i+n] for i in range(0, len(list), n)]

N = int(input())
List = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    A, B = map(int, input().split())

    if A == 1:
        Qt = N // B
        for i in range(1, Qt + 1):
            if List[B * i - 1] == 0:
                List[B * i - 1] = 1
            elif List[B * i - 1] == 1:
                List[B * i - 1] = 0
    else:
        i = 1
        new_List = []
        while 1:
            x = B - 1 - i
            y = B - 1 + i
            if isvaild(x, y, N) and (List[x] == List[y]):
                new_List.append(i)
                i += 1
            else:
                break

        for i in range(0, len(new_List) + 1):
            if List[B + i - 1] == 0:
                List[B + i - 1] = List[B - i - 1] = 1

            elif List[B + i - 1] == 1:
                List[B + i - 1] = List[B - i - 1] = 0

list_result = list_chunk(List, 20)
for result in list_result:
    print(*result)