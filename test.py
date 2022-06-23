print("입력 값 타입 체크")

a = 1
b = "ss"

u = input ("입력하세요 : ")
print("입력 값이 숫자일까? 문자일까?")
print(u)
print("u : ", type(u))
print("a : ", type(a))

# if u == 1 :
if int(u) == 1 :      
    print("같다")
    print("u : ", type(u))
else : 
    print("다르다")