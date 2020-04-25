#parent class
class Person:
      def __init__(self, name, idnumber):
          self.name = name
          self.idnumber = idnumber
          
      def display(self):
          print(self.name)
          print(self.idnumber)

          
#child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        
        #invoking init of parent class
        Person.__init__(self, name, idnumber)
        
    def print_employee_details(self):
        print(self.name, self.idnumber, self.salary, self.post)
        
#creation of an object variable or an instance
person = Person('ed', 9006)
employee = Employee("ed",9006,"xxxx","engineer")

#calling a function of the class person using its instance
person.display()
employee.print_employee_details()
          