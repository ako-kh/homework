# 1.
"""
raxan mocemulobashi asea rom parametrad miigebs sheidzleba amas gulisxmobdit
da komentarad davtoveb
def uppercase(i_string=input("sheiyvanet sityva: ")):
"""
def uppercase(i_string):
    upper_l = 0
    for c in i_string:
        if c.isupper():
            upper_l += 1

    return upper_l, i_string.upper()

print(uppercase(input("sheiyvanet sityva: ")))


# 2.
# def ccase_to_scase(camel_case):
#     snake_case = ""
#     for c in camel_case:
#         if c.isupper():
#             snake_case += "_" + c.lower()
#         else:
#             snake_case += c
#
#     return snake_case
#
# print(ccase_to_scase("preferredFirstName"))
# print(ccase_to_scase("lastName"))
