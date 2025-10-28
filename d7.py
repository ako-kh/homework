# .1
persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33),
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]

while True:
    found = False
    name = input("name: ")
    if name == "stop":
        break

    matched = [p for p in persons if p[0] == name]
    if matched:
       surname = input("surname: ")
       for person in matched:
           if surname == person[1]:
               found = True
               print(person[2])
               break
       else:
           print("no such surname")
    else:
        print("no such name")

    if found:
        break

#.2
w1 = set(input("first word: "))
w2 = set(input("second word: "))

print("saerto", w1.intersection(w2))
print("gansxvavebuli", w1.symmetric_difference(w2))
print("gaertianebuli", w1 | w2)

