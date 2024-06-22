number = int(input('10 ~ 99 사이의 정수를 입력하세요 >>>'))

print('십의 자리 : %d' %(number//10))
print('일의 자리: %d' %(number%10))



month=(int(input('1~12 사이의 월을 입력하세요 >>>')))
list = [31,28,30]

print('{}은 {}일까지 있습니다.' .format(month, list[month-1]))


word = input('영어 단어를 입력하세요 >>>')

dict = {'flower':'꽃', 'fly': '날다', 'floor':'바닥'}
print('{}:{}'.format(word, dict[word]))


traver = set()

travel = input('희망하는 수학여행지를 입력하세요 >>>')
travel = input('희망하는 수학여행지를 입력하세요 >>>')
travel = input('희망하는 수학여행지를 입력하세요 >>>')

print('조사된 수학 여행지는 {} 입니다'.format(travel))