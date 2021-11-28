class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return self.marks > 50

    def __str__(self):
        return self.name


zbyszek: Student = Student('Zbyszek', 60)
janek: Student = Student('Jbyszek', 20)
print(zbyszek.is_passed())
print(janek.is_passed())
