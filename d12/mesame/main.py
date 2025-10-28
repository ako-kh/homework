import csv, faker
from random import randrange

headers = ["ID", "first_name", "last_name", "age"]

fake = faker.Faker()

with open("persons.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for i in range(50):
        writer.writerow({
            "ID": i,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "age": randrange(20, 80)
        })