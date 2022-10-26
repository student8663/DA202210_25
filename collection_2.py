#Fruit class  add remove modify get list exit 
# add : name and positive integer - price
# modify : change the price 
# list : __str__ 

# add two variable  assign key and value 
# remove 
# modify 
# get 
# list 

# if not valid input continue 
# parent loop will be true while loop

from xml.etree.ElementTree import tostring


class FruitInventory():           
    def __init__(self):
        self.myInventory = {

        }

    def addItem(self):
        fruitName = input('Please input the name of the fruit: ')
        fruitPrice = int(input('Please input the price: '))
        self.myInventory[fruitName] = fruitPrice
    
    def removeItem(self):
        userInputForName = input('Please input what you want to remove: ')

        if userInputForName in self.myInventory:
            self.myInventory.pop(userInputForName)
        else:
            print("The item " + userInputForName + " is not in the inventory")
    
    def modifyItemPrice(self):
        userInputForName = input("Please input which price you want to modify: ")

        if userInputForName in self.myInventory:
            userInputForPrice = int(input('Please input new price for ' + userInputForName + ":"))
            self.myInventory.update({userInputForName : userInputForPrice})
        else:
            print('The item ' + userInputForName + " is not in the inventory")

    def getOneItemInfo(self):
        userInputForName = input('Please input which item you want to see: ')

        if userInputForName in self.myInventory:
            itemInfo = userInputForName + ", $" + str(self.myInventory[userInputForName])
            print(itemInfo)
        else:
            print('The item ' + userInputForName + " is not in the inventory")
    
    def __str__(self):
        entireItemInfo = ""
        iterationNum = 1

        for i in self.myInventory:
            entireItemInfo += "Item #" + str(iterationNum) + ":" + " " + i + ", $" + str(self.myInventory[i]) + "\n"
            iterationNum += 1

        return entireItemInfo

user1 = FruitInventory()

while True:    
    userInputForAction = input('Please input add or remove or modify or get or list or exit: ')

    if userInputForAction == "add":
            user1.addItem()
    elif userInputForAction == "remove":
            user1.removeItem()
    elif userInputForAction == "modify":
            user1.modifyItemPrice()
    elif userInputForAction == "get":
            user1.getOneItemInfo()
    elif userInputForAction == "list":
            print(user1)
    elif userInputForAction == "exit":
        break
    else:
        print('Please input valid input ')