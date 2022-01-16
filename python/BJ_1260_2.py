# 백준 1260 DFS와 BFS
# https://www.acmicpc.net/problem/1260
# 다시풀기(촌수계산방식으로 풀어보기)

from collections import deque


def dfs(start):
    q = deque()
    q.append(start)
    visit[start] = 1
    print(start, end = ' ')
    while q:
        d = q.popleft()
        for i in s[d]:
            if visit[i] == 0:
                q.append(i)
                dfs(i)


def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = 0 # dfs에서 visit을 먼저 사용하기 때문에 뒤에서는 0으로 초기화시켜야한다.
    print(start, end = ' ')
    while q:
        d = q.popleft()
        for i in s[d]:
            if visit[i] == 1:
                visit[i] = 0
                print(i, end = ' ')
                q.append(i)


n,m,v = map(int,input().split())

s = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    s[x].append(y)
    s[y].append(x)


dfs(v)
print()
bfs(v)