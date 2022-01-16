# 백준 16948 데스나이트 실버 1
# 다시풀기(210713)

import sys
from collections import deque

input = sys.stdin.readline()

N = int(input().split())
r1, c1, r2, c2 = map(int,input().split())

def bfs(a,b):
    q = deque()
    q.append(a,b)
    visit=[[0]*N for _ in range(N)]
    visit[a][b]=1
    cnt = 0 
    tr,tc = r1,c1
    i=0
    while q:
        cnt += 1
        tr += mr[i]
        tc += mc[i]
        if tr == r2 and tc == c2:
            return cnt
        i+=1


mr = [-2,-2,0,0,2,2] # 이동하는 칸의 수
mc = [-1,+1,-2,+2,-1,+1]