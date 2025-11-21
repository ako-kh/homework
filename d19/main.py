class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"

p1 = Person("Otar", 34)

def person_ser(p_inst):
    return f"Name: {p_inst.name}, Age: {p_inst.age}"

def person_des(string):
    name, age = string.split(",")
    name = name.split()[1]
    age = age.split()[1]
    return Person(name, age)

with open("people.txt", "w") as f:
    f.writelines(person_ser(p1))

with open("people.txt", "r") as f:
    print(person_des(f.readline()))