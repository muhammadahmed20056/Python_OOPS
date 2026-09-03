#Project1
Students=[]
class Student:
    def __init__(self,roll_no=0,name="",marks=0):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks

    def Add(self):
        roll_no=int(input("Enter a roll_no:"))
        name=str(input("Enter a name:"))
        marks=int(input("Enter a marks:"))
        student=Student(roll_no,name,marks)
        Students.append(student)

    def View(self):
        for student in Students:
            print(student.roll_no)
            print(student.name)
            print(student.marks)

    def Search(self):
        roll=int(input("Enter a roll number to search:"))
        for student in Students:
            if student.roll_no == roll:
                print(student.roll_no)
                print(student.name)
                print(student.marks)

    def Update(self):
        roll=int(input("Enter roll number to update:"))
        for student in Students:
           if student.roll_no == roll:
               student.roll_no=int(input("Enter new roll number:"))
               student.name=str(input("Enter new name:"))
               student.marks=int(input("Enter new marks:"))
               print("Student Updated Successfully...")

    def Delete(self):
            roll=int(input("Enter roll number to Delete:"))
            for student in Students:
               if student.roll_no == roll:
                   Students.remove(student)
                   print("Student Deleted Successfully...")

    @staticmethod
    def Grade(marks):
           if marks >= 80:
            return "A"
           elif marks >= 70:
            return "B"
           elif marks >= 60:
            return "C"
           else:
            return "F"
           
   

Student1=Student()

while True:
 print("\t\t\t\t\t\tSTUDENT MANAGEMENT SYSTEM BY USING OOPS CONCEPT:")
 print("MENU")
 print("1.ADD")
 print("2.VIEW")
 print("3.SEARCH")
 print("4.UPDATE")
 print("5.CHECK GRADE")
 print("6.DELETE")
 print("7.EXIT")
 choice=int(input("Enter a choice:"))
 if choice==1:
  Student1.Add()
 elif choice==2:
  Student1.View()
 elif choice==3:
  Student1.Search()
 elif choice==4:
  Student1.Update()
 elif choice == 5:
  roll = int(input("Enter roll number: "))
  for student in Students:
        if student.roll_no == roll:
            grade = Student.Grade(student.marks)
            print("Grade:", grade)
            break

        elif choice==6:
         Student1.Delete()
        elif choice==7:
         print("Exit Program...")
         break
