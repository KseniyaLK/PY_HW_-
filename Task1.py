# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# num = input('введите любое вещественное число-> ')

# a = int(str(num).replace('.', ''))
# def sum_num(n):
#     sum = 0
#     while n!=0:
#         sum = sum + n%10
#         n = n//10
#     print(sum)

# sum_num(a)

num = input('введите любое вещественное число-> ')


def sum_num(n):
    sum = 0
    for i in n:
        if (i != '.') and (i != ','):
            sum += int(i)

    print(sum)


sum_num(num)
