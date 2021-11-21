class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours:str, phone:str):
        self.city :str = city
        self.street :str= street
        self.zip_code :str= zip_code
        self.open_hours :str = open_hours
        self.phone: str = phone

    def __str__(self):
        return 'city: {}\n street: {}\n zip code: {}\n open hours: {}\n phone: {}\n'.format(self.city,self.street,self.zip_code,self.open_hours,self.phone)

class Order:
    def __init__(self,employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return 'employee: {}\n student: {}\n books: {}\n order date: {}\n'.format(self.employee,self.student,self.books,self.order_date )

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name= first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return 'first name: {}\n last name: {}\n hire date: {}\n birth date: {}\n city: {}\n street: {}\n zip code: {}\n phone: {}\n'.format(self.first_name,self.last_name,self.hire_date,self.birth_date,self.city,self.street, self.zip_code,self.phone)

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date= publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages= number_of_pages
    def __str__(self):
        return 'library: {}\n publication date: {}\n author name: {}\n author surname: {}\n number of pages: {}\n'.format(self.library,self.publication_date,self.author_name, self.author_surname,self.number_of_pages)


lib1 = Library('city1','street1','zip_code1','open_hours1','phone1')
lib2 = Library('city2','street2','zip_code2','open_hours2','phone2')

book1 = Book(lib1,'publication1','author1name','author1surname','pages1')
book2 = Book(lib2,'publication2','author2name','author2surname','pages2')
book3 = Book(lib1,'publication3','author3name','author3surname','pages3')
book4 = Book(lib2,'publication4','author4name','author4surname','pages4')
book5 = Book(lib1,'publication5','author5name','author5surname','pages5')

emp1 = Employee('name1','lname1','hire_date1','birth_date1','city1','street1','zip1','phone1')
emp2 = Employee('name2','lname2','hire_date2','birth_date1','city1','street1','zip1','phone2')
emp3 = Employee('name3','lname3','hire_date3','birth_date1','city1','street1','zip1','phone3')

from zadanie1cz2 import Student

student1 = Student('name1',60)
student2 = Student('name1',50)
student3 = Student('name1',20)

order1 = Order(emp3,student3,book5,'order date1')
order2 = Order(emp2,student2,book2,'order date1')

print(order1)
print(order2)



