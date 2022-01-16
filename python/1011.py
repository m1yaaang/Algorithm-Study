
num1=int(input("1st:"))
num2=int(input("2st:"))
op=input("+,-,*,/ : ")


if(op=="+"):
    result=num1+num2
elif(op=="-"):
    result=num1-num2
elif(op=="*"):
    result=num1*num2    
elif(op=="/"):
    result=num1-num2

print("계산결과:",result)

order=int(input("커피 주문 수:"))
pay=order*2000
discount=pay*0.25
print("총금액: ",pay)
print("할인금액: ",discount)
print("총주문금액: ",int(pay-discount))

attend=int(input("출석 "))
mid=int(input("중간 "))
test=int(input("과제 "))
quiz=int(input("퀴즈 "))
final=int(input("기말 "))

score=attend*0.3+mid*0.1+test*0.3+quiz*0.25+final*0.05
print("총점 ",score)

if (score>=90):
    print("90점 이상 True")