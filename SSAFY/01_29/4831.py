# k = 한 번 충전으로 최대 이동 할 수 있는 정류장 
# M = 충전기가 설치된 M 개의 정류장번호
# N = 어디까지 이동할지 

T = int(input())
for case in range(T):
    case += 1
    K, N, M = map(int, input().split())
    List = list(map(int, input().split()))
    count = 0
    