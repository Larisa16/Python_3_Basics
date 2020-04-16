text = "..."

#1) Методами строк очистить текст от знаков препинания
p = ",", ".", "—", "?", ":", ";", "!"
for i in range(len(p)):
    text = text.replace(p[i], "")
print (text)

#2) Cформировать list со словами (split);
text = text.split()
print(text)

#3) Привести все слова к нижнему регистру (map);
text = text.lower()
print(text)

или

text = text.split()
lower_text = list(map(lambda x: x.lower(),text))
print(lower_text)

#4) получить из list пункта 3 dict, ключами которого являются слова,
#а значениями их количество появлений в тексте

dict = {}
for word in text:
    dict[word] = text.count(word)
    dict_text = list(dict.items())
print(dict_text)

# 5) вывести 5 наиболее часто встречающихся слов (sort),
# вывести количество разных слов в тексте (set).

dict_text.sort(key=lambda i: i[1], reverse = True)
top_5 = dict_text[0:5]
print(top_5)

set_of_words = set(text)
nummber_of_words = len(set_of_words)
print(nummber_of_words)