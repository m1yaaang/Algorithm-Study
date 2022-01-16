#백준 13565 침투

from collections import deque
import sys
input = sys.stdin.readline


def bfs(y,x):
    q = deque()
    q.append((y,x))
    graph[y][x]=2
    while q:
        y,x=q.popleft()
        graph[y][x]=2
        for dy,dx in d:
            Y,X = y+dy, x+dx
            if (0<= Y < M) and (0<=X<N) and graph[Y][X]==0:
                q.append((Y,X))
                graph[Y][X] =2




M,N = map(int,input().split()) #2차원 M*N 격자
graph=[list(map(int,list(input().strip()))) for _ in range(M)]
d= [(1,0),(-1,0),(0,1),(0,-1)] #상하좌우 
for j in range(N):
    if(graph[0][j]==0):
        bfs(0,j)

print("YES" if 2 in graph[-1] else "NO")