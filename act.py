#Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.

class Computer:
    def __init__(self):
        self.__max_price=9000

    def display(self):
        print("Cost price is",self.__max_price)

    #setter method
    def setmaxprice(self,price):
        self.__max_price=price

comp1=Computer()
comp1.display()

comp1.__max_price=10000
comp1.display()

comp1.setmaxprice(10000)
comp1.display()