# 백준 16948 데스나이트 실버1

from collections import deque
import sys
input = sys.stdin.readline



def bfs():
    q = deque()
    count = 0
    visit = [[0]*N for _ in range(N)] 
    visit[r1][c1] = 1 
    q.append((r1,c1))
    while q:
        count += 1
        for _ in range(len(q)):
            i,j = q.popleft()
            for a in range(6):
                nr,nc = i+dr[a], j+dc[a]
                if nr == r2 and nc == c2:
                    return count
                if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    q.append((nr,nc))
    return -1


N = int(input()) # 체스판의 크기
r1, c1, r2, c2 = map(int,input().split())

dr = [-2,-2,0,0,2,2]
dc = [-1,+1,-2,+2,-1,+1]

print(bfs())
