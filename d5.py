import random

# .1
# num_list = [2, 5, 8, 32, 65]
# num_sum = 0
#
# for num in num_list:
#     num_sum += num
#
# num_avg = num_sum / len(num_list)
#
# print(f"jami = {num_sum}")
# print(f"sashualo = {num_avg}")

#.2
# mixd_list = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
# no_duplicates = []
#
# for i in mixd_list:
#     if i not in no_duplicates:
#         no_duplicates.append(i)
#
# mixd_list = no_duplicates.copy()
#
# print(mixd_list)
'''
pop metodis gamoyenebas vapirebdi magram bolos ase vamjobine
zedmetad chaxlartuli gamomividoda ise.
tu aris popit an sxva metodit ufro praqtikuli gza
tu shedzleba momweret an gakvetilze axsenit mere madloba

'''


# .3
# num_list = [random.randrange(-50, 50) for _ in range(20)]
# even_num = [i for i in num_list if i % 2 == 0]
# print(num_list)
# print(even_num)


#.4
long_name = []
short_name = []

while True:
    name = input("sheiyvanet saxeli: ")
    if name == "stop":
        break

    name = name.capitalize()
    if len(name) <= 3 :
        short_name.append(name)
    else:
        long_name.append(name)
