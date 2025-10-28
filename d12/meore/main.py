with open("persons.txt") as main_f:
    lines = main_f.readlines()
    for line in lines:
        age = int(line.split(", ")[1])
        if age < 50:
            with open("less.txt", "a") as less_f:
                less_f.write(line)
        else:
            with open("more.txt", "a") as more_f:
                more_f.write(line)
