# .1
tuple_lst = [(1, 3), (4, 2), (2, 5)]

print(sorted(tuple_lst, key = lambda my_tuple: my_tuple[0] + my_tuple[1]))


# .2
# from random import randrange
#
# def make_list(length, a, b):
#     n_lst = [randrange(a, b) for _ in range(length)]
#     try:
#         index = int(input("index: "))
#         print(n_lst[index])
#     except IndexError:
#         print("index does not exist")
#     except ValueError:
#         print("index should be an integer")
#     except Exception as e:
#         print(e)
#
# make_list(5, 4, 12)

# .3
# from functools import reduce
# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 15},
#     {"name": "Keyboard", "price": 25},
#     {"name": "Monitor", "price": 150},
#     {"name": "Power", "price": 100},
#     {"name": "Pad", "price": 10},
# ]
#
# print(
#     "price < 100",
#     list(
#         filter(lambda product: product["price"] < 100, products)
#     )
# )
# print()
# print(
#     list(
#         map(lambda product: product["name"], products)
#     ),
#     list(
#         map(lambda product: product["price"], products)
#     )
# )
# print()
# print(
#     list(
#         sorted(products, key=lambda p: p["price"])
#     )
# )
# print()
# print(
#     "reduce:",
#     reduce(lambda n, p: n + p["price"], products, 0)
# )

# .4
# def sum_f(n):
#     if n <= 0:
#         return n
#     return n + sum_f(n - 1)
#
# print(sum_f(4))