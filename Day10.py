#1st method
# arr = [202, 89, 112, 88]
# output = [sum(int(digit) for digit in str(num)) for num in arr]
# print(output)

# arr = [202, 89, 112, 88]
# output = []

# #2nd method
# arr = [202, 89, 112, 88]
# output = []

# for num in arr:
#     digit_sum = 0
#     for digit in str(num):
#         digit_sum += int(digit)
#     output.append(digit_sum) 

# print(output)

#3rd method
# def sum_digits(input_num):
#     temp = input_num
#     sum = 0
#     while temp > 0:
#         sum += temp % 10
#         temp //= 10
#     return sum

# list1 = [202,89,122,88]
# output = []
# for i in list1:
#     temp_res = sum_digits(i)
#     output.append(temp_res)
#     print(output)
#     # output.append(sum_digits(i))

# def sum_digits(input_num):
#     temp = input_num
#     digit_sum = 0
#     while temp > 0:                                                         #while temp > 0:
#         digit_sum += temp % 10 if (temp % 10) % 2 == 0 else 0               #   digit = temp % 10
#         temp //= 10                                                         #   if 
#     return digit_sum                                                        #   sum += 

# list1 = [202, 89, 112, 88]
# output = []

# for i in list1:
#     temp_res = sum_digits(i)
#     output.append(temp_res)
#     print(output)


list1 = [1, 3, 4, 5, 2]
list2 = [2, 4, 3, 1, 7, 5, 15]

# if all(elem in list2 for elem in list1):
#     print("arr1 is a subset of arr2")
# else:
#     print("arr1 is not a subset of arr2")


# # for elem in list1,list2:
# #     if list1 in list2

# list1 = [1,5,5.5,-32,444,1010]
# search_elem = 5.5

# if search_elem in list1:
#     print("Element exist in list1")
# else:
#     print("Does not exist")

# def search_elem2(input_list,search_elem):
#     for i in input_list:
#         if i == search_elem:
#             return True
#     return False


# list1 = [1, 5, 5.5, -32, 444, 1010]
# search_elem = 5.5

# if search_elem in list1:
#     for i in range(len(list1)):
#         if list1[i] == search_elem:
#             print("Element exists in list1 at index", i)
#             break
# else:
#     print("Does not exist")


def check_subset(list1,list2):
    for i in list1:
        if i not in list2:
            return False
    return True

print(check_subset(list1,list2))