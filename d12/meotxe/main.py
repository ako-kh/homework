import csv


with open("students.csv") as all_students:
    main_f = csv.DictReader(all_students)
    fieldnames = main_f.fieldnames

    with open("failed_students.csv", "w") as failed_students:
        writer = csv.DictWriter(failed_students, fieldnames=fieldnames)
        writer.writeheader()

    with open("passed_students.csv", "w") as passed_students:
        writer = csv.DictWriter(passed_students, fieldnames=fieldnames)
        writer.writeheader()


    for student in main_f:
        if int(student["Grade"]) < 50:
            with open("failed_students.csv", "a") as failed_students:
                writer = csv.DictWriter(failed_students, fieldnames=fieldnames)
                writer.writerow(student)

        else:
            with open("passed_students.csv", "a") as passed_students:
                writer = csv.DictWriter(passed_students, fieldnames=fieldnames)
                writer.writerow(student)