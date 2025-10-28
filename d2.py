# #  .1
# # weight = float(input("your wight in kilograms: "))
# # height = float(input("your height in meters: "))
# #
# # bmi = weight / height ** 2
# # print(bmi)
# # if bmi < 19:
# #     print("underweight")
# # elif bmi < 25:
# #     print("normalweight")
# # else:
# #     print("overweight")
#
# # .2
# x = int(input("first number: "))
# y = int(input("second number: "))
# operation = input("operation (-, +, /, *): ")
#
# if operation == "-":
#     print(x - y)
# elif operation == "+":
#     print(x + y)
# elif operation == "/":
#     print(x / y)
# elif operation == "*":
#     print(x * y)
# else:
#     print("no such operation")
#
# .3
x = int(input("first number: "))
y = int(input("second number: "))
z = int(input("third number: "))

if x == y or x == z or y == z:
    print("numbers should not be same")
else:
    if x > y and x > z:
        print("first is greatest")
    elif y > x and y > z:
        print("second is greatest")
    elif z > x and z > y: #else:
        print("third is greatest")