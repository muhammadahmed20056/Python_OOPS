#Project6
from abc import ABC, abstractmethod
class Payment(ABC):
    def __init__(self,amount=0):
        self.amount=amount


    @abstractmethod
    def Pay(self):
            pass

class Cash_Payment(Payment):
    def Pay(self):
        print("Cash Payment:",self.amount)


class Card_Payment(Payment):
    def Pay(self):
        print("Card Payment",self.amount)

Payments=[]
class PaymentManager:
    def Add(self):
      payment_id=int(input("Enter a id:"))
      customer_name=str(input("Enter a name:"))
      amount=int(input("Enter a amount:"))
      print("1.Cash Payment")
      print("2.Card Payment")
      choice=int(input("Enter a choice:"))
      if choice==1:
            payment=Cash_Payment(amount)
      elif choice==2:
           payment=Card_Payment(amount)
      else:
          print("Invalid enter:")

      Payments.append([payment_id,customer_name,payment])

    def View(self):
        for payment in Payments:
         print("Payment id:",payment[0])
         print("Customer name:",payment[1])
         payment[2].Pay()

    def Search(self):
        id=int(input("Enter id to search:"))
        for payment in Payments:
            if payment[0]==id:
                print("Payment id:",payment[0])
                print("Customer name",payment[1])
                payment[2].Pay()
                return
            
        print("Invalid id:")

    def Update(self):
         id=int(input("Enter id to Update:"))
         for payment in Payments:
            if payment[0]==id:
                payment[0]=int(input("Enter a new id:"))
                payment[1]=str(input("Enter a new name:"))
                payment[2].amount=int(input("Enter a new amount:"))
                print("Details Updated!")
                return
            
         print("Invalid id:")

    def Delete(self):
         id=int(input("Enter id to Delete:"))
         for payment in Payments:
            if payment[0]==id:
                Payments.remove(payment)
                print("Deatails Deleted:")
                return
            
         print("Invalid id:")

Pay = PaymentManager()
while True:
    print("\n===== Payment Management System =====")
    print("1. Add Payment")
    print("2. View Payments")
    print("3. Search Payment")
    print("4. Update Payment")
    print("5. Delete Payment")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Pay.Add()
    elif choice == 2:
        Pay.View()
    elif choice == 3:
        Pay.Search()
    elif choice == 4:
        Pay.Update()
    elif choice == 5:
        Pay.Delete()
    elif choice == 6:
        print("Program Exit...")
        break
    else:
        print("Invalid Choice!")
