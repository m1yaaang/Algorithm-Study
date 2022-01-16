#백준 19583번 사이버개강총회 실버2

#참고 : https://davinci-ai.tistory.com/19
# https://jinyes-tistory.tistory.com/10
# https://wikidocs.net/16#key-keys

import sys
input = sys.stdin.readline


def timeToMinute(time): #시간을 분으로 환산하는 함수 (시간에 100을 곱하여 1130으로 보이게 만듬)
    timeH, timeM = map(int,time.split(':'))
    time = 0
    time = (timeH*100) + timeM 
    return time


S,E,Q = input().split() #시작 시간 S, 끝낸 시간 E, 스트리밍 종료Q
S = timeToMinute(S)
E = timeToMinute(E)
Q = timeToMinute(Q)

attend = {} #참석자를 담을 딕셔너리
cnt = 0

while True:
    try:
        t, i = input().split() #입장시간 t, 닉네임 i
        t = timeToMinute(t)
        
        if t <= S: #입장시간이 시작시간보다 작거나 같으면
            attend[i]=1 #입장
        
        if Q >= t and t >= E: #입장시간이 퇴장시간과 스트리밍 종료시간 사이면
            if attend[i] == 1: #입장한 경우에만 퇴장 기록
                attend[i]=-1 #퇴장

    except:
        break
test = []
for i in attend.keys():
    if attend[i] == -1:
        cnt += 1
        test.append(i)

print(cnt)
print(attend.keys())
print(test)