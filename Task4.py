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
for i in range(len(list_2)):
    dict[list_2[i]] = list_2.count(list_2[i])
frequent = Counter(dict).most_common(1)
print (frequent)

#3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена
#в списке на выходе функции F.

characters = []
for word in list_2:
    characters += word[0]

characters_dict = {}

for character in characters:
    characters_dict[character] = characters.count(character)

print(list(characters_dict)[-1])