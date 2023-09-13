# Булев тип данных true(истина), false(ложь) не заключается в кавычки и начинается с большой буквы
chek = True
chek_1 = False
print(chek_1)

# Операторы сравнения сопастовляют 2 значения и возвращают результат в виде Булева значения.
#  Оператор      операция
#  ==              равно
#  !=             не равно
#  <               меньше
#  >               больше
#  <=          меньше или равно
#  >=          больше или равно

print(1 != 1 )
print(True != False )
print(1 == 1.0)

# Булевы операторы:
#   and   и
#   or   или (вернет True если один из операндов True)
#   not  нет

# Таблица истиности для оператора "end"
# Выражение           результат
# True and True         True
# True and False        False
# False and True        False
# False and False       False

# Выражение               Результат
# True or True             True
# True or False            True
# False or False           False

# Оператор not (нет) (унарный оператор)
# Выражение               Результат
# not True                False
# not False               True

print((4 < 5) and (9 < 6))
print((1 == 5) or (2 == 2))

anna = True
if not True: # if-если. else-иначе. elif-иначе если. ОБЯЗАТЕЛЬНО СТАВИМ ":"
    print("hello anna")
elif anna:
    print("правда")
elif anna == True:
    print('no')
#elif  # иначе-если и содержит блок условий

name = 'anna'
number = 13
if name == 'anna' and number == 13:
    print('vi ugadali')
else:
    print('vi ne ugadali')