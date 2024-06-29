score = int(input('점수를 입력하세요 >>>'))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')



number = int(input('정수를 입력하세요'))

if number % 3 == 0 :
    print('{}는 3의 배수입니다.'.format(number)) 
else:
    print('{}는 3의 배수가 아닙니다'.format(number))  



num_1 = int(input('정수1 입력'))
num_2 = int(input('정수2 입력'))
num_3 = int(input('정수3 입력'))

if num_1 >= num_2 and num_1 >= num_3:
    print('가장 큰 수는 %d입니다.' %num_1)
elif num_2 >= num_1 and num_2 >= num_3:
    print('가장 큰 수는 %d입니다.' %num_2)
else:
    print('가장 큰 수는 %d입니다.' %num_3)



car = input('차량번호를 입력하세요 >>>')

if int(car[-1]) % 2 == 0:
    print('차량번호 {}는 오늘 운행가능입니다.'.format(car))
else:
    print('차량번호 {}는 오늘 운행불가 입니다.'.format(car))

