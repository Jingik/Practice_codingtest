def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_pseudo_palindrome(s, left, right):
    return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)

N = int(input())
for _ in range(N):
    sample = input().strip()
    left, right = 0, len(sample) - 1
    
    while left < right:
        if sample[left] != sample[right]:

            if is_pseudo_palindrome(sample, left, right):
                print(1) 
            else:
                print(2) 
            break
        left += 1
        right -= 1
    else:
        print(0)  
