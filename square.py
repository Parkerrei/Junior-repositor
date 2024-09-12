def sum_square(list):
    sum =0
    for list in list:
        square = list**2
        sum = sum + square
    return sum
list = [12,22,34,2]
print(sum_square(list))


def sum_square(n):
    sum = 0
    for i in range(n+1):
        square = i**2
        sum = sum + square
    return sum
n = 2
print(sum_square(n))



def sum_square(n):
    sum = 0
    for i in range(n+1):
        square = i**2
        sum = sum + square
    return sum
n = 3
print(sum_square(n))    