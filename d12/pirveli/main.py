with open("people.txt", "w") as f:
    count = 1
    while True:
        first_name = input("first name: ").capitalize()
        if first_name == "Stop":
            break
        last_name = input("last name: ").capitalize()


        f.write(f"{count}. {first_name} {last_name}\n")

        count += 1
