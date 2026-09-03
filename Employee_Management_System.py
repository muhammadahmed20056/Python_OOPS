#Project3
list_1=[]
Managers=[]
class Employee:
    def __init__(self,employee_id=0,name="",age=0,salary=0):
        self.employee_id=employee_id
        self.name=name
        self.age=age
        self.salary=salary

    def Add(self):
        employee_id=int(input("Enter a employee id:"))
        name=str(input("Enter a Employee name:"))
        age=int(input("Enter a age:"))
        salary=float(input("Enter a Salary:"))
        emp=Employee(employee_id,name,age,salary)
        list_1.append(emp)
        print("Employee Successfully Added!")

    def View(self):
        for emp in list_1:
            print(emp.employee_id,emp.name,emp.age,emp.salary)

    def Search(self):
        id_emp=int(input("Enter id to search:"))
        for emp in list_1:
            if emp.employee_id==id_emp:
                print(emp.employee_id,emp.name,emp.age,emp.salary)

    def Update(self):
         id_emp=int(input("Enter id to Update:"))
         for emp in list_1:
            if emp.employee_id==id_emp:
                emp.employee_id=int(input("Enter a employee id to update:"))
                emp.name=str(input("Enter a employee name to update:"))
                emp.age=int(input("Enter a age to update:"))
                emp.salary=float(input("Enter a salary to update:"))
                print("Employee Successfully Updated:")

    def Delete(self):
        id_emp=int(input("Enter id to Delete:"))
        for emp in list_1:
            if emp.employee_id==id_emp:
                list_1.remove(emp)
                print("Employee Successfully Deleted!")

class Manager(Employee):
    def __init__(self, employee_id=0, name="", age=0, salary=0,Team_size=0):
        super().__init__(employee_id, name, age, salary)
        self.Team_size=Team_size

    def Add(self):
            employee_id=int(input("Enter a manager id:"))
            name=str(input("Enter a manager name:"))
            age=int(input("Enter a age:"))
            salary=float(input("Enter a Salary:"))
            Team_size=int(input("Enter a team size:"))
            man=Manager(employee_id,name,age,salary,Team_size)
            Managers.append(man)
    
    def View(self):
        for man in Managers:
         print("Manager Details:")
         print("ID:",man.employee_id)
         print("Name:",man.name)
         print("Age:",man.age)
         print("Salary:",man.salary)
         print("Team size:",man.Team_size)

employee = Employee()
manager=Manager()
while True:

    print("\n====================================")
    print("   EMPLOYEE MANAGEMENT SYSTEM")
    print("====================================")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Add Manager")
    print("7. View Managers")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        employee.Add()
    elif choice == 2:
        employee.View()
    elif choice == 3:
        employee.Search()
    elif choice == 4:
        employee.Update()
    elif choice == 5:
        employee.Delete()
    elif choice==6:
        manager.Add()
    elif choice==7:
        manager.View()
    elif choice==8:
        print("Exit Program...")
        break
