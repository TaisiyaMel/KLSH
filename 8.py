#---------------------------------Задание 8-------------------------------------------------------


print('Введите число, по которое включительно будут выписаны все возможные натуральные числа')
print('"число должно быть натуральным"')

number = int(input())

#  заводим пустую строку, чтобы вписать в неё числа от 1 до 4095 включительно переведенные в систему счисления с основанием 4

received_number = ''

# заводим цикл for, чтобы вписать в нашу переменную все числа от 1 до 4095 и сразу же переводим наши числа в систему счисления с основанием 4
for i in range(number, 0, -1):
    number_with_4 = ''
    while i > 0:
        number_with_4 = str(i % 4) + number_with_4
        i = i // 4
    received_number= number_with_4 + received_number

#полученное число переводим в систему счистления с основанием 16 благодаря встроеной функции в питоне hex()
received_number= hex(int(received_number))

#теперь ищем кол-во цифр в полученном числе. создаем счетчик (счетчик начинается с -1, так как при использовании функции hex() к полученному числу прибовляется приставка 0x, и нам нужно учесть этот ноль)
count=-1

# создаем цикл, который будет проверять каждый наш символ, и сравнивать этот символ с цифрой
for i in range(len(received_number)):
    if str(received_number[i]) in '1 2 3 4 5 6 7 8 9 0':
        count+=1

print(count)