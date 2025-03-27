'''Напишите функцию, которая получает два списка в
качестве параметра и возвращает список, содержащий
элементы обоих списков.'''

def add_two_lists(list1, list2):
    for i in range(len(list2)):
        list1.append(list2[i])
    return list1

numbers = input('Введите числа через пробел: ').split()
mylist2 = [int(num) for num in numbers]
numbers1 = input('Введите числа через пробел: ').split()
mylist3 = [int(num) for num in numbers1]
print(f'Объединенный список: {add_two_lists(mylist2, mylist3)}')