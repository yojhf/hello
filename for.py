import random

# for i in range(3):
#     print(i)

for i in range(5) : 
    print(f"{i + 1}.hello world")

    print("짜장면이냐 짬뽕이냐?")

    menu = ["짜장", "짬뽕", "짬짜면"]
    food = input("먹고 싶은거 입력 : ")

    print(f"니가 입력한 값 : {food}") 

    if food == "짜장" or food == "짬뽕":
        print("나오나?????? 나오면 True") 
        print("인공지능이 정해주는 결과는?")
        m = random.choice(menu)   
        print(f"{m} 먹어!!")
    else : 
        print("그래서 뭐 먹을꺼임??? 나오면 False")
