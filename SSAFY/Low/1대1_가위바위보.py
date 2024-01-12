# import sys
#def input():
#    return sys.stdin.readline().strip()
            
A, B = map(int, input().strip().split())

if A == 1:
    if B == 3:
        print("A")
    elif B == 2:
        print("B")

elif A == 2:
    if B == 1:
        print("A")
    elif B == 3:
        print("B")
elif A == 3:
    if B == 1:
        print("B")
    elif B == 2:
        print("A")
        
    
        
