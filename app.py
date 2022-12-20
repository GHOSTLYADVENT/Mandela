class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last= last
        self.pay = pay
        self.email = first + '.' + last + '@' + 'gmail.com'

    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee('Joe', 'Off', 50000)
emp_2 = Employee('Gwen', 'Stacy', 60000)

# print(emp_1.fullname())
print(Employee.fullname(emp_1))