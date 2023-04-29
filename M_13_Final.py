print('Задача 1. Урок информатики 2')


# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
# 
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
# 
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
# 
# Пример 1:
# 
# Введитечисло: 92345
# 
# Формат плавающей точки: x = 9.2345 * 10 ** 4
# 
# Пример 2:
# 
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3

num_x = 0
inc_count = 0

while num_x <= 0:
  num_x = float(input('Введите число больше 0: '))

# Если число больше 10 проводим деление. Точка влево    
  while num_x > 10:   # Делаем только для чисел > 10, если < 10 все уже в нужном виде будет
    inc_count += 1
    num_x /= 10

# В противном случае умножение. Точка вправо
  while num_x < 1:
    inc_count -= 1
    num_x *= 10
  
  num_x = round (num_x, abs(inc_count))
 
print(f'\nФормат плавающей точки: x = {num_x} * 10 ** {inc_count}')

print()

#------------------------------------

print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать. Юрчик захотел написать функцию, которая будет находить максимум из перечисленных чисел. Функция для нахождения максимума из двух чисел у него уже есть. Юра задумался: может быть, её можно как-то использовать для нахождения максимума уже от трёх чисел?

# Помогите Юре написать программу, которая находит максимум из трёх чисел. Для этого используйте только функцию нахождения максимума из двух чисел.

# По итогу в программе должны быть реализованы две функции:
# 1) maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# 2) maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх); при этом она должна использовать для сравнений первую функцию maximum_of_two.


def maximum_of_two (num_a, num_b):
  if num_a > num_b:
    return num_a
  else:
    return num_b


def maximum_of_three (num_a, num_b, num_c):
  num_a = maximum_of_two (num_a, num_b)
  num_a = maximum_of_two (num_a, num_c)
  return num_a

a_num = float(input('Введите первое число: '))
b_num = float(input('Введите второе число: '))
c_num = float(input('Введите третье число: '))

a_num = maximum_of_three (a_num, b_num, c_num)

print('\nМаксимальное число:', a_num)
