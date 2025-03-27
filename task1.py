'''Напишите функцию, вычисляющую произведение
элементов списка целых. Список передаётся в качестве параметра.
Полученный результат возвращается из функции.'''

def multiply_list_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result
list = [1, 3, 5, 2]
print(multiply_list_numbers(*list))