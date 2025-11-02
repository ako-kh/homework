
class Student():
    status = True
    pay = 1000

    def __init__(self, first_name, last_name, age, grades :list):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_discount(self):
        if self.age < 18:
            self.pay -= self.pay * 20 / 100

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)
    
    def get_status(self):
        avg_grade = self.calculate_average()

        if avg_grade > 90:
            return "Excellent"
        elif avg_grade > 70:
            return "Good"
        elif avg_grade > 50:
            return "Average"
        else:
            self.status = False
            return "Poor1"


student = Student("akaki", "khorava", 20, [90, 50])
print(student.get_full_name())
print(student.pay)
student.get_discount()
print(student.pay)
print(student.calculate_average())
print(student.get_status())
print(student.status)