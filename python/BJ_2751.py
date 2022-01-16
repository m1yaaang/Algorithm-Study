#백준 2751 수 정렬하기2 실버5

import sys
input=sys.stdin.readline
write=sys.stdout.write

N = int(input())
A = []

for i in range(N):
    A.append(int(input()))

A.sort()

write('\n'.join(map(str,A)))