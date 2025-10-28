#.1
# n = int(input("input number: "))
# result = 1
# for i in range(n):
#     result *= i+1
# print(result)

#.2
# n1 = 1
# while n1 <= 10:
#     n2 = 1
#     while n2 <= 10:
#         print(f"{n1} * {n2} = {n1*n2}")
#         n2 += 1
#     print("---------")
#     n1 += 1

#.3
price = 50
paid = 0
valid_bill = [5, 10, 20]
while paid < price:
    print(f"gadasaxdelia: {price - paid}")
    bill = int(input(f"moatavset kupiura {valid_bill}: "))
    if bill in valid_bill:
        paid += bill
    else:
        print("moatavset validuri kupiura!")

print(f"gekutvnit {paid - price}")



