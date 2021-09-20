list_data = [1, 2, 3, 4, 5]

# for num in list_data:
#     print(num * 2)
#     print("______" + str(num) + "_______")

# embedded_lists = [[1, 2, 3], [4, 5, 6]]
# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)

dict_data = {1: {"name": "Izah", "age": "29"}, 2: {"name": "Joi", "age": "15"}}
# for key in dict_data:
#     print(key)
#
for dictionary in dict_data.values():
    for value in dictionary.values():
        print(value)

list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in list_data:
    if num % 3 == 0:
        print(num)


list_1 = []

for i in range(1001):
    if i % 2 == 0:
        list_1.append(i)

print(list_1)




