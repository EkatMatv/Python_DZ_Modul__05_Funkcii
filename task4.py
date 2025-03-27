'''Напишите функцию, удаляющую из списка целых
некоторое заданное число. Из функции нужно вернуть
количество удаленных элементов.'''

def del_list_number(mylist, number):
    for num in mylist:
        if num == number:
            mylist.remove(num)
    return mylist
my_list = [3, 5, 7, 13, 9, 24]
print(f'Дан список чисел: {my_list}')
digit = int(input('Введите число, которое нужно удалить: '))
print(f'Обновленный список: {del_list_number(my_list, digit)}')