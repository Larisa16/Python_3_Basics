import random

numbers = list(range(1, 1001))
num = random.choice(numbers)
print("Number is:", num)

# 1) проверка числа на простоту (простые числа - это те числа у которых
# делители единица и они сами);

def IsPrime(num):
    prime = True
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            prime = False
            break
    if prime == True:
        print(num, "is a prime number")
    else:
        print(num, "is a composite number")

IsPrime(num)
# 2) вывод список всех делителей числа;

def GetDivisors(num):
    print("Divisors:", end=" ")
    for i in range(1, num):
        count = 0
        if (num % i == 0):
            for j in range(1, num):
                if (i % j == 0):
                    count_simple = count + 1
            if (count == 0):
                print(i, end=" ")

GetDivisors(num)
# 3) выводит самый большой простой делитель числа;

def Largest_Prime_Divisor(num):
    prime_divisor = 1
    i = 2

    while i <= num / i:
        if num % i == 0:
            prime_divisor = i
            num /= i
        else:
            i += 1

    if prime_divisor < num:
        prime_divisor = num

    return prime_divisor
print("Largest Prime Divisor:", Largest_Prime_Divisor(num))

# 4) функция выводит каноническое разложение числа на простые множители;
def factors(num):
    result = []
    for i in range(2, num):
        while num % i == 0:
            num = num / i
            result.append(i)
            if num == 1:
                break
            if num > 1: result.append(num)
        return print(result)

factors(num)

# 5) функция выводит самый большой делитель (не обязательно простой) числа.
def max_divisor():
    min_divider = num
    max_divider = 1
    for i in range(num - 1, 1, -1):
        if (num % i == 0):
            if (min_divider > i):
                min_divider = i
                if (max_divider < i):
                    max_divider = i
                    return print("Max Divisor:", max_divider)


max_divisor()