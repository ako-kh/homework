#.1
# ar vici amocana sworad gvige tu ara magram mgoni amas itxovdit
# txt = input("winadadeba: ")
# w1 = input("prveli sitryva: ")
# w2 = input("meore sityva: ")
# txt = txt.replace(w1, w2)
# print(txt)

#.2
# txt = input("winadadeba: ")
# txt = txt.split()
# largest_w = ""
# for word in txt:
#     if len(word) > len(largest_w):
#         largest_w = word
#
# print(largest_w)

#.3
w1 = input("prveli sitryva: ").lower()
w2 = input("meore sityva: ").lower()
if len(w1) != len(w2):
    print("ara aris anagrama")
else:
    for i in w1:
        if w1.count(i) != w2.count(i):
            print("ar aris anagrama")
            break
    else:
        print("anagramaa")




