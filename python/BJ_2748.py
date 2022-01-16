# 백준 2748 피보나치 수 2 / 브론즈 1
# https://www.acmicpc.net/problem/2748

def fibo(num):
    s=[0]*100
    s[0]=0
    s[1]=1
    for i in range(2,n+1):
        s[i]=s[i-1]+s[i-2]
    return s[num]
        

n = int(input())
print(fibo(n))
