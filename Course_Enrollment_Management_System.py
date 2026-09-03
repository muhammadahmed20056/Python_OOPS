#Project7
save=[]
class Course:
    def __init__(self,course_id=0,course_name="",fee=0):
        self.course_id=course_id
        self.course_name=course_name
        self.__fee=fee

    @property
    def fee(self):
        return self.__fee

    @fee.setter
    def fee(self,value):
        if value>=0:
            self.__fee=value
        else:
            print("Donot use negative value:")

class Administration(Course):
    def __init__(self, course_id=0, course_name="", fee=0):
        super().__init__(course_id, course_name, fee)

    def Add(self):
        course_id=int(input("Enter a course id:"))
        course_name=str(input("Enter a course name:"))
        fee=int(input("Enter a course fee:"))
        Admin=([course_id,course_name,fee])
        save.append(Admin)
        print("Added Successfully...")

    def View(self):
        for Admin in save:
            print("Course id:",Admin[0])
            print("Course name:",Admin[1])
            print("Course fee:",Admin[2])

    def Search(self):
        id=int(input("Enter a course id to search:"))
        for Admin in save:
            if Admin[0]==id:
                 print("Course id:",Admin[0])
                 print("Course name:",Admin[1])
                 print("Course fee:",Admin[2])

    def Update(self):
        id=int(input("Enter a course id to Update:"))
        for Admin in save:
            if Admin[0]==id:
                Admin[0]=int(input("Enter a course id to update:"))
                Admin[1]=str(input("Enter a course name to update:"))
                Admin[2]=int(input("Enter a course fee to update:"))
                print("Updated Successfully...")
                return
            
        print("Invalid Id:")

def Delete(self):
        id=int(input("Enter a course id to Delete:"))
        for Admin in save:
            if Admin[0]==id:  
                save.remove(Admin)
                print("Delete Successfully!")
                return
            

        print("Invalid Id:")


add=Administration()
while True:
    print("\n===== Course Management System =====") 
    print("1. Add Course") 
    print("2. View Courses") 
    print("3. Search Course") 
    print("4. Update Course") 
    print("5. Delete Course") 
    print("6. Exit") 

    choice = int(input("Enter your choice: ")) 
    if choice == 1: add.Add() 
    elif choice == 2: add.View() 
    elif choice == 3: add.Search() 
    elif choice == 4: add.Update() 
    elif choice == 5: add.Delete() 
    elif choice == 6: 
        print("Program Exit...") 
        break 
    else: 
        print("Invalid Choice!")
        