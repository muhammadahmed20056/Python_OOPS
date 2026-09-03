#Project2
Patients=[]
class Person:
    def __init__(self,name="",age=0):
        self.name=name
        self.age=age

class Patient(Person):
    def __init__(self, name="", age=0,id=0,disease=""):
        super().__init__(name, age)
        self.id=id
        self.disease=disease

    def Add_Patient(self):
        name=str(input("Enter a patient name:"))
        age=int(input("Enter a patient age:"))
        id=int(input("Enter a patient id:"))
        disease=str(input("Enter a patient disease:"))
        patients=Patient(name,age,id,disease)
        Patients.append(patients)

    def View_Pa(self):
        for patients in Patients:
            print(patients.name)
            print(patients.age)
            print(patients.id)
            print(patients.disease)

    def Search_Patient(self):
        p_id=int(input("Enter a patient id to search:"))
        for patients in Patients:
            if patients.id==p_id:
                print(patients.name)
                print(patients.age)
                print(patients.id)
                print(patients.disease)

    def Update_Patient(self):
        p_id=int(input("Enter a Patient id to update:"))
        for patients in Patients:
            if patients.id==p_id:
                patients.name=str(input("Enter a patient name to update:"))
                patients.age=int(input("Enter a patient age to update:"))
                patients.id=int(input("Enter a patient id to update:"))
                patients.disease=str(input("Enter a patient disease to update:"))
                print("Patient Successfully Updated...")

    def Delete_Patient(self):
         p_id=int(input("Enter a Patient id to delete:"))
         for patients in Patients:
            if patients.id==p_id:
                Patients.remove(patients)
                print("Patient Successfully Deleted...")

Doctor=[]
class doctor(Person):
    def __init__(self, name="", age=0,doctor_id=0,specialization=""):
        super().__init__(name, age)
        self.doctor_id=doctor_id
        self.specialization=specialization

    def Add_Doctor(self):
         name=str(input("Enter a doctor name:"))
         age=int(input("Enter a doctor age:"))
         doctor_id=int(input("Enter a doctor id:"))
         specialization=str(input("Enter a doctor specialization:"))
         doc=doctor(name,age,doctor_id,specialization)
         Doctor.append(doc)

    def View_Doc(self):
        for Doc in Doctor:
            print(Doc.name)
            print(Doc.age)
            print(Doc.doctor_id)
            print(Doc.specialization)

    def Search_Doctor(self):
        d_id=int(input("Enter a Doctor id to search:"))
        for Doc in Doctor:
            if Doc.doctor_id==d_id:
                print(Doc.name)
                print(Doc.age)
                print(Doc.doctor_id)
                print(Doc.specialization)

    def Update_Doctor(self):
        d_id=int(input("Enter a Doctor id to update:"))
        for Doc in Doctor:
            if Doc.doctor_id==d_id:
                Doc.name=str(input("Enter a doctor name to update:"))
                Doc.age=int(input("Enter a doctor age to update:"))
                Doc.doctor_id=int(input("Enter a doctor id to update:"))
                Doc.specialization=str(input("Enter a doctor specialization to update:"))
                print("Patient Successfully Updated...")

    def Delete_Doctor(self):
         d_id=int(input("Enter a Doctor id to delete:"))
         for Doc in Doctor:
            if Doc.doctor_id==d_id:
                Doctor.remove(Doc)
                print("Doctor Successfully Deleted...")

class Hospital:
    def __init__(self):
        self.Patients=Patients
        self.Doctors=Doctor

    def View_Patient(self):
        for patient in self.Patients:
            print(patient.name, patient.age, patient.id, patient.disease)

    def View_Doctor(self):
        for doctor in self.Doctors:
            print(doctor.name, doctor.age,
                  doctor.doctor_id, doctor.specialization)


patient = Patient()
Doctor1 = doctor()
hospital = Hospital()
while True:

    print("\t\t\t\t\t\t HOSPITAL MANAGEMENT SYSTEM BY USING OOPS CONCEPT")
    print("MENU")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Add Doctor")
    print("7. View Doctors")
    print("8. Search Doctor")
    print("9. Update Doctor")
    print("10. Delete Doctor")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        patient.Add_Patient()

    elif choice == 2:
        hospital.View_Patient()

    elif choice == 3:
        patient.Search_Patient()

    elif choice == 4:
        patient.Update_Patient()

    elif choice == 5:
        patient.Delete_Patient()

    elif choice == 6:
        Doctor1.Add_Doctor()

    elif choice == 7:
        hospital.View_Doctor()

    elif choice == 8:
        Doctor1.Search_Doctor()

    elif choice == 9:
        Doctor1.Update_Doctor()

    elif choice == 10:
        Doctor1.Delete_Doctor()

    elif choice == 11:
        print("Exit Program...")
        break
