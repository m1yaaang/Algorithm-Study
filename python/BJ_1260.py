# 백준 1260 DFS와 BFS
# https://www.acmicpc.net/problem/1260
# 참고 https://pacific-ocean.tistory.com/260


def dfs(start):
    print(start,end=' ')
    visit[start]=1
    for i in range(1,n+1):
        if visit[i]==0 and s[start][i] == 1: 
            dfs(i)


def bfs(start):
    queue = [start] #큐에 start로 시작하는 배열을 만들어주고
    visit[start]=0 # dfs에서 1로 해줬기 때문에 방문했으면 0 안했으면 1로 설정
    while queue:
        start = queue[0] # start에 큐의 첫번째 요소를 넣어주고 
        print(start,end=' ') # 프린트
        del queue[0] # 프린트 후 지워줌 
        for i in range(1,n+1): 
            if visit[i] == 1 and s[start][i] == 1:
                queue.append(i)
                visit[i]=0 #방문했으면 0 
                


n,m,v = map(int,input().split()) # 정점의개수, 간선의개수, 탐색시작한 정점의 번호
s = [[0]*(n+1)for _ in range(n+1)]
visit=[0 for _ in range(n+1)]

for i in range(m):
    x,y = map(int,input().split())
    s[x][y] =1
    s[y][x] =1

dfs(v)
print()
bfs(v)

