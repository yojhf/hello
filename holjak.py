# AI 컴퓨터가 홀인지 짝인지 문제를 낸다
# 우리가 홀 인지 짝 인지 입력한다
# 내가 입력한 값과 컴퓨터 문제를 낸 값과
# 비교를 해서 맞으면 맞다 틀리면 틀렸다
# 5번 게임을 반복한다

import random


score = 0
life = int(input("목숨 설정 : "))

for i in range(life):    
    ans = ["홀","짝"]
    print("목숨 : ", life)
    print(f"{i+1}번째 게임")
    user = input("홀수 or 짝수를 입력하세요 : ")
    #com = (f"컴퓨터의 선택 : {com}")
    com = random.choice(ans)

    if com == user : 
        score += 100
        print("정답입니다.", com)
        print("점수 : ", score)        
    else  :
        score -= 100
        life -= 1
        print("틀렸습니다.", com)                
        print("점수 : ", score)
        print("목숨 : ", life)
