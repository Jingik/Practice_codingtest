T = int(input())

for i in range(1, T+1):
    A_len, B_len = map(int, input().split())
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))

    Del = abs(A_len - B_len)
    answer = 0

    for j in range(0, Del + 1):
        if A_len > B_len:

            change_A = A_arr[j: j + B_len]

            test = [change_A[k] * B_arr[k] for k in range(len(change_A))]
            test_sum = sum(test)

            if test_sum > answer:
                answer = test_sum
            else:
                answer = answer

        elif A_len < B_len:

            change_B = B_arr[j: j + A_len]

            test = [change_B[k] * A_arr[k] for k in range(len(change_B))]
            test_sum = sum(test)

            if test_sum > answer:
                answer = test_sum
            else:
                answer = answer

    print(f'#{i} {answer}')

