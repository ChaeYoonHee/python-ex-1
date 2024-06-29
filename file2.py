first = float(input('첫 번째 실수를 입력하세요 >>>'))
second = float(input('두 번째 실수를 입력하세요 >>>'))

sum = first + second

print('{}와 {}의 합은 {}입니다.'.format(first, second, sum))



month=(int(input('1~12 사이의 월을 입력하세요 >>>')))
list = [30,28,31,30,31,30,31,31,30,31,30,31]

print('{}은 {}일까지 있습니다.' .format(month, list[month-1]))


word = input('영어 단어를 입력하세요 >>>')

dict = {'flower':'꽃', 'fly': '날다', 'floor':'바닥'}
print('{}:{}'.format(word, dict[word]))


travel = set()

travel_1 = input('희망하는 수학여행지를 입력하세요 >>>')
travel.add(travel_1)
travel_2 = input('희망하는 수학여행지를 입력하세요 >>>')
travel.add(travel_2)
travel_3 = input('희망하는 수학여행지를 입력하세요 >>>')
travel.add(travel_3)

print('조사된 수학 여행지는 {} 입니다'.format(travel))