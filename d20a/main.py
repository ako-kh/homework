import json


number = int(input("how many people to add: "))

with open("persons.json") as f:
    try:
        people = json.load(f)
        next_id = people[-1]["id"] + 1
    except:
        people = []
        next_id = 1

for i in range(number):
    print()
    name = input("name: ")
    age = int(input("age: "))

    people.append(
        {
            "id": next_id,
            "name": name,
            "age": age
        }
    )

    next_id += 1


with open("persons.json", "w") as f:
    json.dump(people, f, indent=4)
