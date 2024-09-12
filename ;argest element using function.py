def find_largest(list1):
    largest = list1[0]
    for x in list1:
        if x > largest:
            largest = x
    return largest
list1= [3,234,34,567]
print(find_largest(list1))


def mymax(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max
list1 = [12,3,45,67]
print("your max value is :", mymax(list1))