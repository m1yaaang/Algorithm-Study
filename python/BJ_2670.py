# 백준 2670 연속부분최대곱 / 실버4
# https://www.acmicpc.net/problem/2670


N = int(input()) # 실수 N
num = [] 
m = 0

for i in range(N):
    num.append(float(input()))

for i in range(N):
    if (i==0):
        m=num[0]
    else:
        num[i] = max(num[i-1]*num[i],num[i])
        # arr[i-1]*arr[i]가 arr[i]보다 크다면, arr[i]를 갱신한다
        m = max(m,num[i])
        # arr[i]가 max값보다 크다면 max를 갱신한다

print("%.3f" % m)
