#Project5
list=[]
class Restaurant:
    total_product=0

    def __init__(self,product_id=0,name="",price=0,quantity=0):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.quantity=quantity

    def Add(self):
        product_id=int(input("Enter a Product id:"))
        name=str(input("Enter a name:"))
        price=int(input("Enter a price:"))
        quantity=int(input("Enter a quantity:"))
        menu=Restaurant(product_id,name,price,quantity)
        list.append(menu)
        print("Product Added.")
        Restaurant.total_product+=1

    def View(self):
        for menu in list:
            print(menu.product_id,menu.name,menu.price,menu.quantity)

    def Search(self):
        id=int(input("Enter Product id to search:"))
        for menu in list:
            if menu.product_id==id:
             print(menu.product_id,menu.name,menu.price,menu.quantity)
             return
            

    def Update(self):
         id=int(input("Enter Product id to Updated:"))
         for menu in list:
            if menu.product_id==id:
                menu.product_id=int(input("Enter a updated id:"))
                menu.name=str(input("Enter a updated name:"))
                menu.price=int(input("Enter a updated price:"))
                menu.quantity=int(input("Enter a quantity:"))
                print("Product Updated!")
                return
            
            else:
             print("Product Not Found.")

    def Delete(self):
        id=int(input("Enter Product id to Delete:"))
        for menu in list:
            if menu.product_id==id:
                list.remove(menu)
                Restaurant.total_product-=1
                return
            
            else:
             print("Product Not Found!")

    @classmethod
    def Total_Product(cls):
       print("Total Product",cls.total_product)
      

res=Restaurant()
while True:
    print("\n================================")
    print("     RESTAURANT MANAGEMENT")
    print("================================")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Total Products")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        res.Add()

    elif choice == 2:
        res.View()

    elif choice == 3:
        res.Search()

    elif choice == 4:
        res.Update()

    elif choice == 5:
        res.Delete()

    elif choice == 6:
        Restaurant.Total_Product()

    elif choice == 7:
        print("Exit Program...")
        break
    else:
        print("Invalid Choice!")
