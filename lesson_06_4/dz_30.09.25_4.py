# Є лист з числами, порахуйте суму усіх ПАРНИХ чисел в цьому листі

lst = [7, 9, 12, 13, 2, 6, 9, 5]
list2 = []
for item in lst:
    if item % 2 == 0:
        list2.append(item)
print(sum(list2))


list2 = [item for item in lst if item % 2 == 0]
print(sum(list2))


list2 = (sum(item for item in lst if item % 2 == 0))
print(list2)


# ТРЕНУЮСЬ

# lst = [7, 9, 12, 13, 2, 6, 9, 5]
# list2 = []
# for item in lst:
#     if item % 2 == 0:
#         list2.append(0)
#     else:
#         list2.append(item)
# print(len(list2))
# print(max(list2))
# print(list2)
#
# list2 = [0 if item % 2 == 0 else item for item in lst]
# print(len(list2))
# print(max(list2))
# print(list2)