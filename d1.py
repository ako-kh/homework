# k1 = int(input("კათეტი 1: "))
# k2 = int(input("კათეტი 2: "))
# h = (k1 ** 2 + k2 ** 2) ** (1 / 2)
# a = (k1 * k2) / 2
# print(f"ჰიპოტენუზა= {h}")
# print(f"ფართობი= {a}")
#
seconds = int(input("წამების რაოდენობა: "))
string = f"{seconds} წამი არის "

if seconds / 3600 > 1:
    remaining = seconds % 3600
    hours = (seconds - remaining) // 3600
    seconds = remaining
    string += f"{hours} საათი, "
if seconds / 60 > 1:
    remaining = seconds % 60
    minutes = (seconds - remaining) // 60
    seconds = remaining
    string += f"{minutes} წუთი, "
if seconds > 0 :
    string += f"{seconds} წამი"

print(string)

