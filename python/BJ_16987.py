#백준 16987 계란으로 계란치기 실버1

import sys
input = sys.stdin.readline()

N = int(input()) #계란수 N(1<=N<=8)
S,W = [],[] #내구도 S, 무게 W
b = [1 for _ in range(N)]
cnt = 0 #최대 계란수

for _ in range(N):
    s,w = map(int,input.split())
    S.append(s)
    W.append(w)

for i in range(N):
    
    j = 1
    while j<N:
        weight1 = S[i]-W[j]
        weight2 = S[j]-W[i]
        if weight1<=0 & weight2<=0:
            
            j+=1

