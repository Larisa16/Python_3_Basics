'''
#Задача 1
#Вывести на экран 5 строк из нулей, причем каждая из строк должна быть пронумерована
s=0; i=0
while i <=4 :
    i=i+1
    s = 0
    print ((i), (s))

#Задача 2
#Пользователь в цикле вводит 10 цифр, Найти количество введенных пользователем цифр 5.
count = 0
for i in range (10):
    number = input('Введите любую цифру от 0 до 9: ')
    if int(number) == 5:
        count += 1
print('Количество введенных цифр "5":' , count)

#Задача 3
#Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран
s=0; i=1
while i<=100:
    s+=i
    i+=1
print (s)

#Задача 4
#Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран

number=10
sum=1
for i in range(1, number + 1):
        sum = sum*i
print(sum)

# Задача 5
# Вывести цифры числа на каждой строчке.
number = 3456
numberStr=str(number)
for char in numberStr:
    print (char)

# Задача 6
# Найти сумму цифр числа
num = int(input("Enter number: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("The sum of digits is:", sum)

# Задача 7
# Найти произведение цифр числа.(для примера использовано четырёхзначное число)
n = int(input ('Введите четырехзначное число :'))
s = str(n)
a = int (s[0])
b = int (s[1])
c = int (s[2])
d = int (s[3])
print (a*b*c*d)

#Задача 8
#Дать ответ на вопрос: есть ли среди цифр числа 5?

integer_number = 213416
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

#Задача 9
#Найти максимальную цифру в числе
a=input("Enter number: ")
m = max([int(i) for i in str(a)])
print (m)

#Задача 10
#Найти количество цифр 5 в числе
int_number = 546789555
count_5 = 0
while int_number>0:
    if int_number%10 == 5:
        count_5 += 1
    int_number = int_number//10
print('Количество цифр "5":', count_5)

'''

