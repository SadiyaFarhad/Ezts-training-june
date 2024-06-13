"""
Create class Carshowroom in which user should select car company  then its car models and  select variant 
Total price is calculated based on sgst, sgst,variant and car company model.
"""
class Car:
    def _init_(self):
        self.cgst = 5555
        self.sgst = 5555
        
    def company(self):
        while True:
            print("Available companies: Toyota, Mercedes")
            self.n = input("Enter car company: ")
            if self.n.lower() == "toyota":
                print("Welcome to Toyota")
                self.model(self.n)
                break
            elif self.n.lower() == "mercedes":
                print("Welcome to Mercedes")
                self.model(self.n)
                break
            else:
                print("Please enter a valid company")
    
    def model(self, company):
        if company.lower() == "toyota":
            models = ["Fortuner", "CC"]
        elif company.lower() == "mercedes":
            models = ["amg", "gw"]
        
        while True:
            print(f"Available models for {company}: {', '.join(models)}")
            self.choice = input("Enter car model: ")
            if self.choice in models:
                self.variant(self.choice)
                break
            else:
                print("Please enter a valid model")
    
    def variant(self, choice):
        variants = ["Petrol", "Diesel"]
        while True:
            print(f"Available variants for {choice}: {', '.join(variants)}")
            self.var_choice = input("Enter car variant (Petrol/Diesel): ")
            if self.var_choice in variants:
                self.price(choice, self.var_choice)
                break
            else:
                print("Please enter a valid variant")

    def price(self, choice, var_choice):
        # Base prices for different models
        if choice == "Fortuner":
            base_price = 4500000
        elif choice == "CC":
            base_price = 1000000
        elif choice == "amg":
            base_price = 24432874
        elif choice == "gw":
            base_price = 843726835
        else:
            print("Invalid model choice")
            return
        
        # Additional price based on variant
        if var_choice == "Petrol":
            var_price = 50000
        elif var_choice == "Diesel":
            var_price = 60000
        self.cgst=5555
        self.sgst=5555
        total_price = base_price + var_price + self.sgst + self.cgst
        print(f"Total price including taxes and variant cost: {total_price}")

c = Car()
c.company()
"""
OUTPUT:Available companies: Toyota, Mercedes
Enter car company: toyota
Welcome to Toyota
Available models for toyota: Fortuner, CC
Enter car model: CC
Available variants for CC: Petrol, Diesel
Enter car variant (Petrol/Diesel): Diesel
Total price including taxes and variant cost: 1071110
"""