with open('vocabulary.txt','a') as f:
    while True:
        word = input('영어 단어를 입력하세요: ')
        if word == 'q':
            break
        k_word = input('한국어 뜻을 입력하세요: ')
        if k_word == 'q':
            break
        f.write(word +': '+k_word+'\n')

# with open('vocabulary.txt','r') as f:
#     for line in f:
#         word,k_word = line.split(': ')
#         answer = input('{}: '.format(word))
#         if answer == k_word:
#             print('맞았습니다!\n')
#         else:
#             print('아쉽습니다. 정답은 {}입니다.\n'.foramt(k_word))