from audioop import reverse
from os import remove

from numpy import insert, append, sort

# Работа со строками
# 1

string1 = "This is a string."
string2 = " This is another string. "
# 2
string3 = string1 + string2
print(string3)
# 3
print(len(string2))
print(string3.title())
print(string3.lower())
print(string3.upper())
print(string3.rstrip())
print(string3.lstrip())
print(string3.strip())
print(string3.strip('T'))
# 4
d = "qwerty"
ch = d[2]  # извлекается символ ‘e’
print(ch)
print(d)
# 5
chm = d[1:3]
print(chm)
# 6
chm = d[1:]
print(chm)
chm = d[:3]
print(chm)
chm = d[:]
print(chm)
chm = d[1:5:2]
print(chm)
# 7
# d[2]='o'
# print(d)

# Работа с числами

int1 = 5
int2 = 10
int3 = int1 / int2
print(int3)
int3 = int1 % int2
print(int3)
int3 = int1 ** int2
print(int3)

# param = "string" + 15
param = "string" + str(15)
print(param)

# Преобразование данных
# 1
param = "string" + str(15)

# 2
# n1 = input("Enter the first number: ")
# n2 = input("Enter the second number: ")
# n3 = float(n1) + float(n2)
# print(str(n1) + " plus " + str(n2) + " = ", str(n3))

# Форматирование строк
# 2
a = 1 / 3
print("{:7.3f}".format(a))

# 3
a = 2 / 3
b = 2 / 9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

# 4
# n1 = float(input("Enter the first number: "))
# n2 = float(input("Enter the second number: "))
# n3 = n1 + n2
# print("{:7.3f} plus {:7.3f} = {:7.3f}".format(n1, n2, n3))

# Списки
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
# dir(list)
# help(insert)
# help(append)
# help(sort)
# help(remove)
# help(reverse)
list1[3] = 100
print(list1)
list1.append(200)
print(list1)
list1.insert(5, 343)
print(list1)
list1.remove(343)
print(list1)
list1.pop()
print(list1)

#
