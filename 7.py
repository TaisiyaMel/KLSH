#---------------------------------Задание 7-------------------------------------------------------


from math import sqrt                

print('введите длины сторон треугольника')
a , b ,c = map(float, input().split())   

print('введите радиус окружности')
R=float(input()) 

# находим полупериметр 
p=(a+b+c)/2 

# находим площадь треугольника через формулу герона
s=sqrt(p*(p-a)*(p-b)*(p-c))

# находим радиус через формулу для радиуса описанной около треугольника окружности
R_triangle=(a*b*c)/(4*s)

# сравниваем радиус который дан с радиусом треугольник, логично, что если полученный будет меньше и равен тому который дан, то окружность будет покрывать треугольник
if R>=R_triangle:
    print('покрывает')
else:
    print(0)