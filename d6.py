
# #.1
# my_dict = {n: n*n for n in range(1,11)}
# print(my_dict)

# #.2
# products = [
#     {"cola": {
#         "price": 1.5,
#         "quantity": 10
#     }},
#     {"fanta": {
#         "price": 2.5,
#         "quantity": 5
#     }},
#     {"snickers": {
#         "price": 3.5,
#         "quantity": 12
#     }},
#     {"water": {
#         "price": 4.5,
#         "quantity": 8
#     }},
#     {"beer": {
#         "price": 6.5,
#         "quantity": 5
#     }}
# ]
#
# total = 0
# for product in products:
#     name, = product
#     print(f'name: {name}')
#     total += product[name]["price"] * product[name]["quantity"]
#
# print(f"total: {total}")

#.3
fruits = {}

while True:
    fruit = input("fruit: ").lower()
    if fruit == "stop":
        break

    fruits[fruit] = fruits.get(fruit, 0) + 1

print(fruits)