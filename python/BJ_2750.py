#백준 2750 수 정렬하기 브론즈1

N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

A.sort()

for i in range(N):
    print(A[i])