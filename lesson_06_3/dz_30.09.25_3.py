# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0,
# 'Lorem Ipsum']. Напишіть код, який свормує новий list (наприклад lst2), який містить лише
# змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [item for item in lst1 if isinstance(item, str)]
print(lst2)

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for item in lst1:
    if isinstance(item, str):
        lst2.append(item)
print(lst2)

# тренуюсь

# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# lst_numbers = []
# for item in lst1:
#     if isinstance(item, int) and not isinstance(item, bool):
#         lst_numbers.append(item)
# print(lst_numbers)
#
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# lst_numbers = []
# for item in lst1:
#     if isinstance(item, bool):
#         lst_numbers.append(item)
# print(lst_numbers)
#
# lst = [True, 'True', False, 'False', 1, 0, 'Yes', 'No']
# lst1 = []
# for item in lst:
#     if isinstance(item, bool):
#         lst1.append(item)
# print(lst1)
#
# lst = [3, '7', 8, '2', 10, 'Python', 5, 6]
# lst1 = []
# for item in lst:
#     if isinstance(item, int) and item > 5:
#         lst1.append(item)
# print(lst1)
#
# lst = ['1', 2, True, 'False', 3.14, None, 'Hello', False, 0]
# lst1 = []
# lst2 = []
# lst3 = []
# lst4 = []
# lst5 = []
# for item in lst:
#     if isinstance(item, int) and not isinstance(item, bool):
#         lst1.append(item)
#     if isinstance(item, float):
#         lst2.append(item)
#     if isinstance(item, bool):
#         lst3.append(item)
#     if isinstance(item, str):
#         lst4.append(item)
#     if item is None:
#         lst5.append(item)
# print(len(lst1))
# print(len(lst2))
# print(len(lst3))
# print(len(lst4))
# print(len(lst5))






