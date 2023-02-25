#---------------------------------Задание 5-------------------------------------------------------


# если граф имеет больше двух нечетных вершин, то обход, при котором ребро проходится не больше одного раза, невозможен.
# если граф имеет только четные вешины, то обход возможен.
# если граф имеет две нечетные вершины, и путь начинается на одной из этих вершин, то обход возможен
# если граф имеет нечетное количество нечетных вершин, то такой граф не существует


# вводим счетчик нечетных вершин 
count_odd_tops=0  
quantity_road_start=0


# узнаем где начинается путь
print('введите откуда Настя начинает свой путь (флаг/первый корпус/второй корпус/третий корпус/лес/столовая/медпункт)')           
place_start=input()                                   


# если количество дорог нечетно, то добавляем к нашему счетчику 1, и четность/нечетность вершины начала нашего пути 
print('введите количество дорог исходящих из флага')       
quantity=int(input())                                      
if quantity%2!=0:
    count_odd_tops+=1
    if 'флаг'==place_start:
        quantity_road_start=quantity


print('введите количество дорог исходящих из леса')
quantity=int(input())
if quantity%2!=0:
    count_odd_tops+=1
    if 'лес'==place_start:
        quantity_road_start=quantity


print('введите количество дорог исходящих из медпункта')
quantity=int(input())
if quantity%2!=0:
    count_odd_tops+=1
    if 'медпункт'==place_start:
        quantity_road_start=quantity


print('введите количество дорог исходящих из столовой')
quantity=int(input())
if quantity%2!=0:
    count_odd_tops+=1
    if 'столовая'==place_start:
        quantity_road_start=quantity


print('введите количество дорог исходящих из первого корпуса')
quantity=int(input())
if quantity%2!=0:
    count_odd_tops+=1
    if 'первый корпус'==place_start:
        quantity_road_start=quantity


print('введите количество дорог исходящих из второго корпуса')
quantity=int(input())
if quantity%2!=0:
    count_odd_tops+=1
    if 'второй корпус'==place_start:
        quantity_road_start=quantity


print('введите количество дорог исходящих из третьего корпуса')
quantity=int(input())
if quantity%2!=0:
    count_odd_tops+=1
    if 'третий корпус'==place_start:
        quantity_road_start=quantity


#проверяем наши условия для ответа на задачу
if count_odd_tops==0:
    print('возможно')
    
elif count_odd_tops%2!=0:
    print('такой граф не сущетвует')
    
elif  count_odd_tops>2:                                         
    print('невозможно')
    
elif count_odd_tops==2 and  quantity_road_start%2!=0:
    print('возможно')
    
else:
    print('невозможно')
