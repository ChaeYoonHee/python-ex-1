def vending_machine(money):
    coin = 700
    count = money // 700
    change = 0
    for n in range(count+1):
        change = money - n*coin
        print('음료수 = {}개, 잔돈 = {}원'.format(n,change))
vending_machine(3000)


#def get_average(marks):


#marks = {'국어':90, '영어':80,'수학':85}
#print('평균은 {}점 입니다.'. format(average))


