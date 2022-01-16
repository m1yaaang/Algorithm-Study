# 백준 2644 촌수계산 실버2
# https://www.acmicpc.net/problem/2644
# 참고 https://pacific-ocean.tistory.com/321

from collections import deque #큐 구현 FIFO
import sys
input = sys.stdin.readline

n = int(input()) # 전체 사람 수 
a, b = map(int,input().split()) # 촌수 계산할 사람 2명 
m = int(input()) # 부모자식들의 관계 수
s = [[] for i in range(n+1)] # 노드들을 담을 트리
result = [0 for i in range(n+1)] # 사람별 관계도 입력

def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for i in range(n + 1)]
    visit[start] = 1
    while q:
        d = q.popleft() # pop은 오른쪽에서, popleft는 왼쪽
        for i in s[d]:
            if visit[i] == 0:
                visit[i] = 1
                result[i] = result[d] + 1 # 0부터 시작해서 찾고자하는 사람의 촌수 1 증가 
                q.append(i)
                
for i in range(m):
    x, y = map(int, input().split())
    s[x].append(y)
    s[y].append(x)

bfs(a)
print(result[b] if result[b] != 0 else -1)

