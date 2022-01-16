# 백준 4963 섬의 개수 실버2

import sys
from collections import deque

input = sys.stdin.readline

w,h = map(int,input().split()) # 너비 w, 높이 h

def bfs(a,b):
    q=deque()
    q.append((a,b))
    
    visit=[[0]*w for _ in range(h)]
    for i in range(w):
        for j in range(h):
            if island[i][j] == 1:
                visit[i][j] = 1
                
            

    while q:
        d=q.popleft()
        if visit[d]



while w!= 0 and h!=0:
    island = [[0]*w for _ in range(h)]
    for i in range(h):
        island[i]=int(input().split())

