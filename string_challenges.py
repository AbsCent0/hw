# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[10:])


# Вывести количество букв "а" в слове
word = 'Архангельск'
a = word.lower()
print(a.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
a = word.lower()
glasn = "аеёиоуыэюя"
count = 0
for i in a:
    if i in glasn:
        count += 1
print(count)    


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
a = sentence.split()
print(len(a))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
a = sentence.split()
for let in a:
    print(let[:1])



# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
a = sentence.split()
f = 0
for let in a:
    f += len(let)
    sred = f/len(a)
print(sred)