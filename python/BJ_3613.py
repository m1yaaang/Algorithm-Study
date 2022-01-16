# 백준 3613 Java vs C++ / 실버5

import sys
input = sys.stdin.readline
user_word = input()

def c_word(word):
    word = word.replace('_',' ')
    word = word.title()
    word = word[0].lower()+word[1:]
    word = word.replace(' ','')
    return word.strip()



def java_word(word):
    for i in range(len(word)):
        if word[i].isupper():
            word =  word.replace(word[i],'_'+word[i].lower())
    return word.strip()

code = 0

if user_word.find('_') > 0: # C++ 변수명일때
    for i in range(len(user_word)): # C++ 변수명 안에 대문자가 있을 경우
        if user_word[i].isupper():
            code = -1 #에러일 경우
            break
        else : code = 1 #c++변수명일때 자바 출력
else:
    for i in range(len(user_word)): # java 변수명일때
        if user_word[i].isupper():
                if user_word.find('_') > 0:
                    code = -1
                    break   
                else: code = 2
                break


if code == -1: print('Error!')
elif code == 1: print(c_word(user_word))
elif code == 2: print(java_word(user_word))
