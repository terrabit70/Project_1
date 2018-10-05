# -*- coding: utf-8 -*-

import random

print('******************************')
print('*         Угадай число       *')
print('*          от 0 до 20        *')
print('*         за 6 попыток       *')
print('******************************')

count = 6
secret_number = random.randint(0, 20)

while count > 0:
    print('Попыток осталось: ', count)
    print('Число мне запили: ', end='')
    input_number = input()
    if not input_number.isdigit():
        print('Ты втираешь мне какую-то дичь!')
    else:
        if int(input_number) > secret_number:
            print('Жадность фраера сгубила!')
        elif int(input_number) < secret_number:
            print('Маловато! Маловато будет!')
        else:
            print('Заебись, чотко!')
            break
    count -= 1
else:
    print('Потрачено!')
