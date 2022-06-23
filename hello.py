import random

print("Hello World")
print("짜장면이냐 짬뽕이냐?")

# 만약에 짜장과 짬뽕 둘중에 하나 추천
# 내가 짜장이나 짬뽕을 적으면 짜장이나 짬뽕중에서
# 아니면 둘다(짬짜?)

menu = ["짜장", "짬뽕", "짬짜면"]
food = input("먹고 싶은거 입력 : ")

# print("니가 입력한 값 : ", food)
# print("니가 입력한 값 : %s"%food)
# print("니가 입력한 값 : {0}".format(food))
print(f"니가 입력한 값 : {food}") # 이 방식을 선호

if food == "짜장" or food == "짬뽕":
    print("나오나?????? 나오면 True") # 참 일때만 나옴
    # 여기서 짜장과 짬뽕중에
    # 인공지능이 추천 해주는 결과는?
    print("인공지능이 정해주는 결과는?")
    m = random.choice(menu)   
    print(f"{m} 먹어!!")
else : 
    print("그래서 뭐 먹을꺼임??? 나오면 False")

    


# '''

# '''

