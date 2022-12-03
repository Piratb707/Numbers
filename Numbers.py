
import random

tryce = 0

print('Как тебя зовут ?')

myName = input()

number = random.randint(1,20)
print('Ну чтож , ' + myName + 'хочешь выиграть миллион , угадай число от 1 до 20')

for tryce in range(6):
  print('Ну угадай.')
  popitka = input('Напиши число: ')
  popitka = int(popitka)

  if popitka < number:
    print('Твоё число слишком маленькое.')

  if popitka > number:
    print('Твоё число слишком большое.')

  if popitka == number:
      break

if popitka == number:
  tryce = str(tryce + 1)
  print('Отлично ' + myName + '! Ты справился за ' + tryce + 'попытки!')

if popitka != number:
  number = str(number)
  print('Лошара. Я загодал число' +number+'.') 
