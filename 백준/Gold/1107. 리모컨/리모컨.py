from sys import stdin

MAX = 10 ** 6
dest = int(input())
num_of_broken = int(input())
broken = []

# 고장난 버튼의 개수가 0이 아닌 경우
if num_of_broken:
	broken = stdin.readline().split()

if dest == 100:
	print(0)
else:
	# moves 초기값: dest에서 + or - 로만 이동하는 경우
	moves = abs(dest - 100)
    
    # 0 - 1,000,001 까지의 범위 탐색
	for channel_int in range(MAX + 1):
		channel = str(channel_int)
        
        # channel의 각 자릿수에 접근 
		for idx, ch in enumerate(channel):
        	# broken에 포함된 숫자이면 break
			if ch in broken:
				break
            
            # broken에 포함되지 않고 모든 자릿수까지 탐색한 경우
			elif idx == len(channel)-1:
            	# ex) dest: 5457, num_of_broken: 3, broken: 6, 7, 8
                # 5455 or 5459 에서 접근하는 것이 빠름
                # (5457 - 5455) + 4(5455가 네자리)
                # (dest - channel) + len(channel)
                # channel값이 매번 바뀌기 때문에 최솟값을 저장해두고 비교해서 가장 작은 값을 도출해야함
				moves = min(moves, abs(dest-channel_int)+len(channel))
	print(moves)