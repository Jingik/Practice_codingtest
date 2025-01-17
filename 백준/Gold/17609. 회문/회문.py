import sys
input = sys.stdin.readline

def is_palindrome(a):
    return a[::-1] == a

def is_pseudo_pal(a):
    if len(a) == 2:
        return True
    if is_palindrome(a[1:]) or is_palindrome(a[:-1]):
        return True
    if a[0] != a[-1]:
        return False
    diff_i = 1
    for i in range(1,len(a)//2):
        if a[i] != a[~i]:
            diff_i = i
            break

    return is_pseudo_pal(a[diff_i:~diff_i+1])
T = int(input())
for _ in range(T):
    s = input().rstrip()
    ans = 2
    if is_palindrome(s):
        ans = 0
    elif is_pseudo_pal(s):
        ans = 1
    print(ans)

