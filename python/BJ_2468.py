# 백준 2468 안전영역 실버1
# https://www.acmicpc.net/problem/2468

from collections import deque
import sys
input = sys.stdin.readline

N = int(input().split()) #행과 열의 크기
s = [0 for i in range(N+1)] # 노드들을 담을 트리
safty_map = [[] for i in range(N+1)]

for i in range(N):
    safty_map[i]=map(int(),input().split())
    