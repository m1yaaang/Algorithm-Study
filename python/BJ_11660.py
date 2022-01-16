# 백준 11660 구간 합 구하기5 /실버1
# https://www.acmicpc.net/problem/11660
# 참고 https://backtony.github.io/algorithm/2021/02/21/algorithm-boj-class4-29/

import sys

input = sys.stdin.readline

N,M = map(int,input().split()) #표의 크기 N / 합을 구해야 하는 횟수 M

dp =[] #표
op = []

for i in range(N): # 표 받기
    dp.append(list(map(int,input().split())))

for i in range(N): # 각 행의 누적 합
    for j in range(1,N):
        dp[i][j] += dp[i][j-1]

for i in range(1,N): # 각 열의 누적 합
    for j in range(N):
        dp[i][j] += dp[i-1][j]
        

for i in range(M): # 더할 합계 받기
    x1,y1,x2,y2 = map(int,input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    # 첫 행, 첫 열
    if y1 == 0 and x1 ==0:
        ans = dp[x2][y2]
    # 첫 행
    elif x1 == 0:
        ans = dp[x2][y2] - dp[x2][y1-1]
    # 첫 열
    elif y1 == 0:
        ans = dp[x2][y2] - dp[x1-1][y2]
    else:
        ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    op.append(ans)

for i in range(M):
    print(op[i])
            

