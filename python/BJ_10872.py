#백준 팩토리얼 브론즈3 재귀

import sys
input = sys.stdin.readline

N = int(input())

result = 1

def Factorial(n):
    global result
    if(n > 1):
        return n * Factorial(n-1)
    else:
        return 1

print(Factorial(N))