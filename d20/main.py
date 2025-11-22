import json, faker, random

fk = faker.Faker()
students = []

for _ in range(0,100):
    students.append(
        {
            "first_name": fk.first_name(),
            "last_name": fk.last_name(),
            "email": fk.email(),
            "age": random.randrange(18, 70),
            "is_active": bool(random.randrange(0,2))
        }
    )
print(students)
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)


with open("students.json", "r") as f:
   students1 = json.load(f)

active = [i for i in students1 if i["is_active"]]

with open("active_students.json", "w") as f:
    json.dump(active, f, indent=4)