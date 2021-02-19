class Employee:
    no_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + '@email.com'
        Employee.no_of_emps+=1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)


emp_1 = Employee("vishwas", "luhana", 5000)
emp_2 = Employee("sarmad", "talpur", 6000)

print(emp_1.email)
