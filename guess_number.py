import random

print('******************************')
print('*         Угадай число       *')
print('*          от 0 до 20        *')
print('*         за 6 попыток       *')
print('******************************')

count = 6
zag_val = random.randint(0, 20)

while count > 0:
    print('Попыток осталось: ', count)
    print('Число мне запили: ', end='')
    inp_val = input()
    if inp_val.isdigit() == False:
        print('Ты втираешь мне какую-то дичь!')
    else:
        if int(inp_val) > zag_val:
            print('Жадность фраера сгубила!')
        elif int(inp_val) < zag_val:
            print('Маловато! Маловато будет!')
        else:
            print('Заебись, чотко!')
            break
    count -= 1
else:
    print('Потрачено!')
