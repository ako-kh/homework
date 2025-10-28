# .1
# def sum_num(quantity=5):
#     return_n = 0
#     for _ in range(quantity):
#         return_n += int(input("sheiyvanet ricxvi: "))
#     return return_n
#
# print("ricxvebis jami =", sum_num())

# .2
# def odd_even(*args):
#     odd = []
#     even = []
#     for n in args:
#         if n % 2 != 0:
#             odd.append(n)
#         else:
#             even.append(n)
#     return odd, even
#
# print(odd_even(1,2,3,4,3,4,5,6,7))

# .3
def count_words(text):
    text = text.lower().split()
    w_count = {}

    for word in text:
        word = "".join([c for c in word if c.isalpha()]) # mxolod asoebis datoveba

        if word in w_count:
            w_count[word] += 1
        else:
            w_count[word] = 1
    return w_count

print(count_words("This is a test. This test is fun"))