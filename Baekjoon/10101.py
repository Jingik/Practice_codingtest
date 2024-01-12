a = int(input())
b = int(input())
c = int(input()) # 3줄에 걸쳐 삼각형의 각의 크기를 입력받음

if((a+b+c)!=180): # 세 각의 합이 180이 아닌 경우
  print("Error")
elif(a==60 and b==60 and c==60): # 세 각의 크기가 모두 60인 경우
  print("Equilateral")
elif((a+b+c)==180 and (a==b or b==c or a==c)): # 세 각의 합이 180이고, 두 각이 같은 경우
  print("Isosceles")
elif((a+b+c)==180)and (a!=b and b!=c and a!=c): # 세 각의 합이 180이고, 같은 각이 없는 경우
  print("Scalene")