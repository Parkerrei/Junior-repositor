
user = int(input("enter any number"))
list = []
for i in range(user):
    if i % 3 or i % 5 == 0:
        list.append(i)
        i += 1
print(i)
        


# def divisible_by (num):
#     for num in range(num):
#         if num % 3 and num % 5 == 0:
#             print(num,end = "")
# num = 50
# print(divisible_by(num))


# def print_divisible_numbers(n):
#     for num in range(n):
#         if num %  3 and num % 5 == 0:
#             print(num,end = "")
# n = 50
# print(print_divisible_numbers(n))

# n = 50
# result = [i for i in range(n) if i % 3 and i % 5 == 0]
# print(result)