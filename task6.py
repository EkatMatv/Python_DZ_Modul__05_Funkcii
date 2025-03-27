'''Напишите функцию, высчитывающую степень каждого
элемента списка целых. Значение для степени передаётся
в качестве параметра, список тоже передаётся в качестве
параметра. Функция возвращает новый список, содержащий полученные результаты.'''


def power_numbers_list(list1, pow):
    mylist = []
    for i in range(len(list1)):
        mylist.append(list1[i]**pow)
    return mylist
numbers = input('Введите числа через пробел: ').split()
my_list = [int(num) for num in numbers]
pow = int(input('Введите степень для чисел: '))
print(f'Список {my_list}, возведенный в степень {pow}: {power_numbers_list(my_list, pow)}')
