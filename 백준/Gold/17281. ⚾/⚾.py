from itertools import permutations

n = int(input())

innings = []
for i in range(n):
    innings.append(list(map(int,input().split())))
    
def progress(sign):
    global score, out, base_1, base_2, base_3
    if sign == 0:
        out += 1
    elif sign == 1:
        score += base_3
        base_3 = base_2
        base_2 = base_1
        base_1 = 1
    elif sign == 2:
        score += (base_3 + base_2)
        base_3 = base_1
        base_2 = 1
        base_1 = 0
    elif sign == 3:
        score += (base_3 + base_2 + base_1)
        base_3 = 1
        base_2 = 0
        base_1 = 0
    elif sign == 4:
        score += (base_3 + base_2 + base_1 + 1)
        base_3 = 0
        base_2 = 0
        base_1 = 0
    
    
def game(players):
    global score
    hitter = 0
    score = 0
    
    for inning in innings:
        global out, base_1, base_2, base_3
        out = 0
        base_1, base_2, base_3 = 0, 0, 0
        
        while out<3 :
            progress(inning[players[hitter]])
            hitter = (hitter+1)%9
                
    return score    
   
max_score = 0
    
p_list = list(permutations(range(1,9), 8))
for p in p_list:
    players = list(p[:3]) + [0] + list(p[3:])
    max_score = max(max_score, game(players))

print(max_score)