# # 1) Пользователь вводит строку.
_str = input('Введите строку: ')
# # 1.1 Сначала выведите третий символ этой строки.
print('третий символ этой строки:', _str[2])
# # 1.2 Во второй строке выведите предпоследний символ этой строки.
print('предпоследний символ этой строки:', _str[-2])
# # 1.3 В третьей строке выведите первые пять символов этой строки.
print('первые пять символов этой строки:', _str[:5])
# # 1.4 В четвертой строке выведите всю строку, кроме последних двух символов.
print('вся строка без последних двух симворов:', _str[:-2])
# # 1.5 В пятой строке выведите все символы с четными индексами
# #     (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
print('символы с четными индексами:',_str[::2])
#     print('все символы с четными индексами:', i)
# # 1.6 В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.

print('все символы с нечетными индексами:',_str[1::2])
# # 1.7 В седьмой строке выведите все символы в обратном порядке.
print('все символы в обратном порядке: ', _str[::-1])
# # 1.8 В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.

print('все символы строки через один в обратном порядке', _str[-1:0:-2])
# # 1.9 В девятой строке выведите длину данной строки.
# print('длина данной строки: ', len(_str))
# #
# 2) Пользователь вводит две строки. Необходимо определить, являются ли две строки анаграммами.
#    Анаграмма — это слова состоящие из одних и тех же букв, расположенных в разном порядке.
_str1 = input('Введите первую строку:')
_str2 = input('Введите вторую строку:')
_str1 = sorted(_str1)
_str2 = sorted(_str2)
if _str2 == _str1:
    print('анаграмма')
else:
     print('это разные слова')
# 3) Пользователь вводит строку и символ. Определить количество вхождений символа в строку, независимо от регистра.
_str = input('введите тестовую строку:')
_symbol = input('введите искомый символ:')
_count = 0
for i in _str:
    if i == _symbol:
        _count +=1
print('количество вхождений символа в строку',_count)
# # 4) Пользователь вводит  строку и символ.
# #    Необходимо определить индексы первого и последнего вхождения символа в строке.
_str = input('введите тестовую строку:')
_symbol = input('введите искомый символ:')


a = _str.find(_symbol)
b = _str.rfind(_symbol)
if a == -1:
    print()
elif a == b:
    print(a)
else:
    print(a, b)
#
#
# 5) Пользователь вводит строку. Необходимо определить, являются ли строка палиндромом, также учитывать,
#    что строка помимо букв, может содержать пробел, тире, запятую, точку, восклицательный и вопросительный знак.
# Палиндром — слово или текст, одинаково читающееся в обоих направлениях.
_str5 = input('Проверочная строка: ')
l = len(_str5)
for i in range(l):
    if _str5[i] != _str5[-1-i]:
        print('Это не палиндром')
        quit()
print('Это палиндром')
