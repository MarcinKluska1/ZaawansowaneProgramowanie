from OrderModels.Order import Order
from OrderModels.Employee import Employee
from OrderModels.Library import Library
from OrderModels.Student import Student
from OrderModels.Book import Book


lib1 = Library('city1', 'street1', 'zip_code1', 'open_hours1', 'phone1')
lib2 = Library('city2', 'street2', 'zip_code2', 'open_hours2', 'phone2')

book1 = Book(lib1, 'publication1', 'author1name', 'author1surname', 'pages1')
book2 = Book(lib2, 'publication2', 'author2name', 'author2surname', 'pages2')
book3 = Book(lib1, 'publication3', 'author3name', 'author3surname', 'pages3')
book4 = Book(lib2, 'publication4', 'author4name', 'author4surname', 'pages4')
book5 = Book(lib1, 'publication5', 'author5name', 'author5surname', 'pages5')

emp1 = Employee('name1',
                'lname1',
                'hire_date1',
                'birth_date1',
                'city1',
                'street1',
                'zip1',
                'phone1')
emp2 = Employee('name2',
                'lname2',
                'hire_date2',
                'birth_date1',
                'city1',
                'street1',
                'zip1',
                'phone2')
emp3 = Employee('name3',
                'lname3',
                'hire_date3',
                'birth_date1',
                'city1',
                'street1',
                'zip1',
                'phone3')

student1 = Student('name1', 60)
student2 = Student('name1', 50)
student3 = Student('name1', 20)

order1 = Order(emp3, student3, book5, 'order date1')
order2 = Order(emp2, student2, book2, 'order date1')

print('order 1:\n{}'.format(order1))
print('order 1:\n{}'.format(order2))
