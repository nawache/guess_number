from random import randint


WELCOME_TEXT = 'Угадайте число от 1 до 100'

print(WELCOME_TEXT)
number = randint(1, 100)

while True:
    guess = int(input('Введите число: '))

    if guess < number:
        print('Ваше число меньше того, что загадано.')
    elif guess > number:
        print('Ваше число больше того, что загадано.')
    elif guess == number:
        break

print('Отличная интуиция! Вы угадали число :)')
