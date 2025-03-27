'''Напишите функцию, определяющую количество простых чисел в списке целых.
Список передаётся в качестве параметра. Полученный результат возвращается
из функции.'''

def simple_list_numbers(*args):
    prime_count = 0
    for num in args:
        if num <= 1:
            continue
        elif num == 2 or num == 3:
            prime_count += 1
        elif num % 2 == 0 or num % 3 == 0:
            continue
        else:
            is_prime = True
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    is_prime = False
                    break
                i += 6
            if is_prime:
                prime_count += 1
    return prime_count

my_list = [2, 5, 7, 8, 3, 78, 29, 36, 76, 94, 97, 67, 25, 17]
print(simple_list_numbers(*my_list))