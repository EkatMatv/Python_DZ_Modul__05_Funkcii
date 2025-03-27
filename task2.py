'''Напишите функцию для нахождения минимума в
списке целых. Список передаётся в качестве параметра.
Полученный результат возвращается из функции.'''

def min_list_numbers(*args):
    if not args:
        return 'Список пуст'
    min_num = args[0]
    for num in args:
        if num < min_num:
            min_num = num
    return min_num
my_list = [34, 56, 45, 12, 67, 98]
print(f'Минимальное значение из списка {my_list}: {min_list_numbers(*my_list)}')

