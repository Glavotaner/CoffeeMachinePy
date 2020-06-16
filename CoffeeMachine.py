REQUIREMENTS = {
    'coffee': [500, 50, 250],
    'cappucinno': [300, 100, 250],
    'latte': [300, 200, 150]
}


class CoffeeMachine:
    """Constructors"""
    def __init__(self,coffee_amount: int, milk_amount: int, water_amount: int):
        self.coffee_amount = coffee_amount
        self.milk_amount = milk_amount
        self.water_amount = water_amount
        self.coffeeGunk = 0
        self.power = {"On": False, "Off": True}
        
    @property 
    def coffee_amount(self):
        return self.__coffee_amount    
    @coffee_amount.setter
    def coffee_amount(self, coffee_amount: int):
        if 0 <= coffee_amount <= 3000:
            self.__coffee_amount = coffee_amount
    
    @property
    def milk_amount(self):
        return self.__milk_amount
    @milk_amount.setter
    def milk_amount(self, milk_amount: int):
        if 0 <= milk_amount <= 500:
            self.__milk_amount = milk_amount   
    
    @property
    def water_amount(self):
        return self.__water_amount
    @water_amount.setter
    def water_amount(self, water_amount: int):
         if 0 <= water_amount <= 2000:
            self.__water_amount = water_amount 
    
    """Constructors end"""           
                     
    def __str__(self):
        return f"""Daisy1605 Coffee Machine
    
Powered on: {self.power["On"]} 

Coffee amount: {self.coffee_amount}
Milk amount: {self.milk_amount}
Water amount: {self.water_amount}"""

    def addIngredients(self, _coffee_amount: int, _milk_amount: int, _water_amount: int):
        if self.coffee_amount > _coffee_amount + self.coffee_amount or _coffee_amount + self.coffee_amount > 3000:
            print("Inadequate amount of coffee\n")
        else:
            self.coffee_amount += _coffee_amount
            
        if self.milk_amount > _milk_amount + self.milk_amount or _milk_amount + self.milk_amount> 500:
            print("Inadequate amount of milk\n")
        else:
            self.milk_amount += _milk_amount
            
        if self.water_amount > _water_amount + self.water_amount or _water_amount + self.water_amount > 2000:
            print("Inadequate amount of water\n")
        else:
            self.water_amount += _water_amount
    
    def makeThing(self, _type_of_coffee: str):
        global REQUIREMENTS
        
        if not _type_of_coffee in REQUIREMENTS.keys():
            return "I can't make that"
        
        print(self)
    
    def togglePower(self):
        if self.coffeeGunk > 10:
            return "Naaaaaah you best be cleaning me first niqqa"
            
        elif self.power["On"]:
            self.power["On"] = False
            self.power["Off"] = True
            return "Powered off"
        else:
            self.power["On"] = True
            self.power["Off"] = False
            return "Powered On!"
    
    def runMachine(self):
        while self.power["On"]:
            print(f"""With:
                  
{self.coffee_amount} grams of coffee
{self.milk_amount} ml of milk
{self.water_amount} ml of water
        
you can make
things.
        
Do you want to continue?
        """)
            #answer = str(input(".."))
            answer = "No"
            if answer == "No":
                self.power["On"] = False
        
        print(f"""Ok, what do you want to make?

Cappucinno
Coffee
Latte
""")    
        type_of_coffee = str(input("Type of thing: "))
        

machine1 = CoffeeMachine(3000, 500, 1500)
machine2 = CoffeeMachine(2000, 250, 1000)

machine1.togglePower()
machine1.addIngredients(0, 20, 500)
print(machine1)

machine2.togglePower()
machine2.addIngredients(50, 100, 200)
print(machine2)
