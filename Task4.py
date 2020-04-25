#Задание 4

from random import choices
from collections import Counter

#1. Напишите функцию (F): на вход список имен и целое число N; на выходе список
#длины N случайных имен из первого списка (могут повторяться, можно взять значения:
#количество имен 20, N = 100, рекомендуется использовать функцию random);

list_1 = ['Winnie', 'Christopher', 'Robin', 'Piglet', 'Eeyore', 'Kanga', 'Roo', 'Tigger', 'Rabbit', 'Owl', 'Dorothy', 'Bill', 'Eureka', 'Toto', 'Scarecrow', 'Mowgli','Bagheera', 'Baloo', 'Kaa','Akela']
def names_choice(names, quantity):
    return choices(names, k = quantity)
list_2 = names_choice(list_1, 100) #получаем новый список из 100 имен
print(list_2)

#2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

dict = {}
#for i in range(len(list_2)):
    #dict[list_2[i]] = list_2.count(list_2[i])
#frequent = Counter(dict).most_common(1)
#print (frequent)
def most_frequent(list_2):
    counter = 0
    num = list_2[0]
    for i in list_2:
        most_frequent = list_2.count(i)
    if(most_frequent > counter):
        counter = most_frequent
        num = i
    return num
print(most_frequent(list_2))

#3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена
#в списке на выходе функции F.

def unique(list_2):
    list_unique = []
    for k in list_2:
        list_unique += k[0]
        for i in list_unique:
            dict[i] = list_unique.count(i)
        list_unique = list(dict.items())
        list_unique.sort(key=lambda i: i[1])
        return (list_unique[0][0])
print(unique(list_2))