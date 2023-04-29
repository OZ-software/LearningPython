print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N 
# и выводит сумму всех чисел от 1 до N включительно.
# 
# Пример работы программы:
# Введите число: 5
# 
# Я знаю, что сумма чисел от 1 до 5 равна 15

def summa_n(num):
  summ = 0
  for i in range (1, num + 1):
    summ += i
  print(f'Я знаю, что сумма всех чисел от 1 до {num} равна {summ}')


num = int(input('Введите все число: '))
summa_n(num)

print()
#----------------------------------------------
print('Задача 2. Функция в функции')

# Евгений проходит специальный тест по программированию.
# У него всё шло хорошо, пока он не наткнулся на тему “Функции”.
# 
# Задание звучит так:
# Основная ветка программы, не считая заголовков функций, состоит из одной строки кода.
# 
# Это вызов функции test().
# В ней запрашивается на ввод целое число.
# Если оно положительное, то вызывается функция positive(),
# тело которой содержит команду вывода на экран слова "Положительное".
# 
# Если число отрицательное, то вызывается функция negative(),
# ее тело содержит выражение вывода на экран слова "Отрицательное".
# 
# Помогите Евгению и реализуйте такую программ

print()

def test ():
  number = int(input('Введите целое число: '))
  
  if number > 0:
    positive()
  elif number < 0:
    negative()
  else:
    zero()

def positive():
  print('\nПоложительное')

def negative():
  print('\nОтрицательное')

def zero():
  print('\nНуль')

test()

print()


#----------------------------------------------
print('Задача 3. Апгрейд калькулятора')

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия. 
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру. 

#Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.
import math


# Поиск максимальной цифры

def max_num (number):      
  max_n = 0
  number = abs(number)
    
  if number % 1 != 0:  # Если число дробное убираем дробную часть
    number = get_count(number)
  else:
    number = int(number) # Чтобы при выводе все было красиво, если на вход подали целое число, сделаем из него целое
    
    
  # А теперь, что бы здесь ни было ищем максимальную цифру в числе
  while number != 0:
    current_n = number % 10
    
    if current_n >= max_n:
      max_n = current_n 
    
    number //= 10 
  
  print('Максимальная цифра в вашем числе равна', max_n)

# Поиск минимальной цифры

def min_num (number):
  min_n = 9
  number = abs(number)
  max_f = 0  # Число разрядов после . По умолчанию считаем, что число целое.
  
  if number % 1 != 0:  # Если число дробное убираем дробную часть
    number = get_count(number) 
  else:
    number = int(number) # Чтобы при выводе все было красиво, если на вход подали целое число, сделаем из него целое

    
  # А теперь, что бы здесь ни было ищем минимальную цифру в числе
  while number != 0:
    current_n = number % 10
    
    if current_n <= min_n:
      min_n = current_n 
    
    number //= 10 
  
  print('Минимальная цифра в вашем числе равна', min_n)

      
# Сумма цифр

def sum_num (number):
  summ = 0
  number = abs(number)
  max_f = 0  # Число разрядов после . По умолчанию считаем, что число целое.
  
  if number % 1 != 0:  # Если число дробное убираем дробную часть
    number = get_count(number)
  else:
    number = int(number) # Чтобы при выводе все было красиво, если на вход подали целое число, сделаем из него целое
    
  # А теперь просто складываем цифры
  while number != 0:
    current_n = number % 10
    summ += number % 10
       
    number //= 10 
  
  print('Сумма цифер в вашем числе равна', summ)

# Функция которая убирает дробную часть присоединяя ее к целой для дальнейших операций
  
def get_count(number):
  max_f = 0  # Для подсчета разядра числа после .
  fractional = number
  
  s = str(number)
  if '.' in s:
    max_f = abs(s.find('.') - len(s)) - 1 # получили количество разрядов после запятой
    fractional *= 10 ** max_f
    fractional = int (fractional)  # нужно убрать все дробные остатки, которые возникают из-за округления
    return fractional

operation = 0
while True:
  current_number = float(input('\nВведите любое число для которого будет проводится операция: '))
  
  while True:
    operation = int(input('\nВведите номер операции, где 1 - поиск максимальной цифры, 2 - поиск минимальной цифры, 3 - поиск суммы цифер: '))
    if 0 < operation < 4:
      break
  
  if operation == 1:
    max_num (current_number)
  elif operation == 2:
    min_num (current_number)
  else:
    sum_num (current_number)
 
#----------------------------------------------
print('Задача 4. Число наоборот')

# Вводится последовательность чисел,
# которая оканчивается нулём.
#
# Реализуйте функцию,
# которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.

# Пример:
# Введите число: 1234
# Число наоборот: 4321
# 
# Введите число: 1000
# Число наоборот: 0001
# 
# Введите число: 0
# Программа завершена!
# 
# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.
# 
# Введите число: 1230
# Число наоборот: 321
# 
# Кстати, нули, которые мы убрали, называются ведущими.
import math

def reverse_num (number_f):
  number_r = ''    # Обратное число
  
  if number_f < 0:    # Приписываем минус, если изначальное число отрицательное
    number_r = '-'
  
  number_f = abs(number_f)
  number_f = str(number_f)
  

  for num in range (len(number_f)-1, -1, -1):
    number_r += number_f[num]
  number_r = int(number_r)
  print ('Число наоборот:', number_r)

number_f = 0

while True:
  print()
  number_f = int(input('Введите целое число. "0" - остановка ввода: '))
  if number_f == 0:
    print('Программа завершена.')  
    break
    
  reverse_num (number_f)

print()


#----------------------------------------------
