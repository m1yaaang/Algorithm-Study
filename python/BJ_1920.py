#백준 1920 수찾기 실버4

import sys
input = sys.stdin.readline

N = int(input()) 
A = list(map(int,input().split()))
M = int(input())
S = list(map(int,input().split()))

A.sort()

for i in S:
    check = 0
    start,end = 0,len(A)-1
    while start <= end:
        result = 0
        mid = (start + end) //2
        if A[mid] == i:
            result = 1
            break
        elif A[mid] > i:
            end = mid - 1
        elif A[mid] < i:
            start = mid +1
    print(result)