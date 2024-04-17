# Вычисляем значение выражения
value = 9**7 + 3**21 - 19

# Переводим в систему счисления с основанием 3
base3 = ""
while value > 0:
    base3 = str(value % 3) + base3
    value //= 3

# Считаем количество цифр "2"
count = base3.count("2")

print(count)
