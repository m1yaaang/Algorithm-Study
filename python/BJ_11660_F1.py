# 백준 11660 구간 합 구하기5 /실버1
# https://www.acmicpc.net/problem/11660
# 시간초과

def sum(x1,y1,x2,y2):
    total = 0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            total += arr[i-1][j-1]
            j+=1
        i+=1 
    return total   

data = list(map(int,input().split())) #표의 크기 N / 합을 구해야 하는 횟수 M

N = data[0]
M = data[1]

arr = []
ord = []

for i in range(N): # 표 받기
    arr.append(list(map(int,input().split())))

for i in range(M): # 더할 합계 받기
    ord.append(list(map(int,input().split())))


for i in range(M):
    print(sum(ord[i][0],ord[i][1],ord[i][2],ord[i][3]))

