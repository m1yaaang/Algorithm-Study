# 코드잇 고급 사전
import random

vocab = {}
with open('vocabulary.txt','r') as f:

    for line in f:
        data = line.strip().split(': ')
        word,k_word=data[0],data[1]
        vocab[word] = k_word

keys = list(vocab.keys())
size = len(keys)
while True:
    num = random.randint(0,size-1)
    eng_word = keys[num]
    kor_word = vocab[eng_word]
    answer = input('{}: '.format(eng_word))
    if answer == kor_word:
        print("맞았습니다!")
    elif answer == 'q':
        break
    else:
        print('틀렸습니다. 정답은 {}입니다.'.format(kor_word))
    