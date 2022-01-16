# 백준 2644 촌수계산 다시 해보기(210707)
# https://www.acmicpc.net/problem/2644


import sys
from collections import deque 
input = sys.stdin.readline


n = int(input()) # 사람수
a,b = map(int,input().split()) # 관계를 구할 2명
m = int(input()) # 관계수

s = [[] for i in range(n+1)] # 관계를 담을 노드
result = [0 for i in range(n+1)]



def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for _ in range(n+1)]
    visit[start] = 1
    while q:
        d = q.popleft()   
        for i in s[d]:
            if visit[i] == 0:
                visit[i]=1
                result[i]=result[d]+1
                q.append(i)


for i in range(m):
    x,y = map(int,input().split())
    s[x].append(y)
    s[y].append(x)

bfs(a)
print(result[b] if result[b]!=0 else -1)