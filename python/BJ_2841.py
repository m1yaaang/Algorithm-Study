#백준 2841 외계인의 기타 연주 실버1 스택

import sys
input = sys.stdin.readline

N,P = map(int,input().split()) #멜로디의 음 N, 한 줄의 프렛 P
cnt = 0 #움직임
melody = [[]for _ in range(7)]

# n,p=map(int,input().split()) #음 n, 프렛 p


for i in range(N):
    n,p=map(int,input().split()) #음 n, 프렛 p
    if(len(melody[n])>0):
        while(melody[n][len(melody[n])-1]>p): #전 프렛이 다음 프렛보다 큰 경우
            melody[n].pop()
            cnt += 1
            if(len(melody[n])<=0): #stack이 empty면
                break
        if(len(melody[n])!=0):
            if(melody[n][len(melody[n])-1]!=p):  
                melody[n].append(p)
                cnt += 1
        else:                
            melody[n].append(p)
            cnt += 1
    else:
        melody[n].append(p)
        cnt += 1

print(cnt)
