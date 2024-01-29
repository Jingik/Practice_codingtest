T=int(input())

for i in range (T):
    N=int(input())
    count_ai=[]
    ai=list(map(str,input()))
    
    #카드 몇장인지 count()
    
    for j in range(N):
        cnt=ai.count(ai[j])
        count_ai.append(cnt)
        
    count_max=0
    
    #카드 장수가 같으면 적힌 숫자가 가장 큰 쪽을 출력한다
    for c in count_ai:
        if c == max(count_ai):
            count_max += 1
            
    if count_max > 1:
        result = []
        for index,c in enumerate(count_ai):
            if c == max(count_ai):
                result.append(index)
        final_result = 0
        for k in result:
            if final_result < ai[k]:
                final_result = ai[k]
        print(f'#{i+1} {final_result} {max(count_ai)}')
    else:
        index = count_ai.find(max(count_ai))
        print(f'#{i+1} {ai[index]} {max(count_ai)}')
            
    # if count_ai.count(max(count_ai)) > ai.count(ai[count_ai.index(max(count_ai))]):
    #     print(f'#{i+1} {max(ai)} {max(count_ai)}')
    # else:
    #     print(f'#{i+1} {ai[count_ai.index(count_max)]} {max(count_ai)}')