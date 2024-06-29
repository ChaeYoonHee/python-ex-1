money = 10000
on = 0

while True:
    print('현재 {}원이 있습니다.'.format(money))
    if money == 0:
        break
    on = int(input('사용할 금액 입력 >>>'))
    if on <= 0:
        print('0 이하의 금액은 사용할 수 없습니다.')
    elif on > money:
        print('{}원이 부족합니다.'.format(on - money))
    else:
        money -= on
    


while True:
    movie = int(input('이번 영화의 평점을 입력하세요 >>>'))
    if movie >= 1 and movie <= 5:
       print('평점:{}'.format('⭐' * movie))
       break
    else:
        print('평점은 1~5 사이만 입력할 수 있습니다.')


key = 'qwerty'
count = 0

while True:
    count += 1
    password = input('비밀번호를 입력하세요')
    if password == key:
        print('비밀번호를 맞혔습니다')
        break
    if count == 5:
        print('비밀번호 입력 횟수를 초과했습니다.')
        break


for dan in range(3, 10, 2):
    for n in range(1, dan, +1):
        print(f'{dan}x{n}={dan*n}')

    print('')
    