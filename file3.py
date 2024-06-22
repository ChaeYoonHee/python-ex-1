number = int(input('10 ~ 99 사이의 정수를 입력하세요 >>>'))

print('십의 자리 : %d' %(number//10))
print('일의 자리: %d' %(number%10))



time = int(input('초를 입력하세요 >>>'))

hour = time // 3600
minute = time % 3600 // 60
second = time % 60

print('변환 결과는 {}시간 {}분 {}초 입니다.'.format(hour, minute, second))



num = int(input('4자리 사원번호를 입력하세요 >>>'))

last_num = num % 10

result = '오전' if (last_num >= 5) else '오후'

print('근무시간은 {}입니다.'.format(result))


box_1 = 20
print('한 박스에 {}개의 라면을 담을 수 있습니다.'.format(box_1))
print('라면의 개수를 입력하시면 필요한 박스 수를 알려 드립니다.')

ramen = int(input('라면의 개수를 입력하세요 >>>'))

box = ramen// box_1 if (ramen % box_1 == 0) else ramen // box_1 + 1

print('{}개의 라면을 담으려면 {}박스가 필요합니다'.format(ramen, box))



score_1 = int(input('국어 점수를 입력하세요 >>>'))
score_2 = int(input('영어 점수를 입력하세요 >>>'))
score_3 = int(input('수학 점수를 입력하세요 >>>'))

average = (score_1 + score_2 + score_3) / 3
result = '합격' if (average >= 80) else '불합격'

print('평균은 {}점이고, 결과는 {}입니다.'.format(average, result))