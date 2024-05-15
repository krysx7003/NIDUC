import os
from ..simulationElements.Shop import Shop
from ..simulationElements.Customer import Client
from .SettingsConst import SettingsConst as CONST

class Setting:
    _instance = None

    # Singletone method for class Setting 
    def __new__(cls):
        if (cls._instance is None):
            cls._instance = super().__new__(cls)            
            cls._instance.__init__()
        return cls._instance 

    # Constructor of Setting class, class handles the simulation settings 
    def __init__(self):
        self.__client = Client() 
        self.__shop =Shop() 

    # Function prints the options of setting Menu
    def printOptionMenu(self): 
        for i in range(len(CONST.SETTINGS_MAIN_MENU)):
            print(i+1,  CONST.SETTINGS_MAIN_MENU[i])


    # Functions is a runner which invokes in order the methods of the classs
    def settingMenuRunner(self, actionType):
        print("Chose element which settings to print/set")
        self.printOptionMenu()
        print("Enter relevant number: ")
        if actionType == 1:
            self.menuPirntControler(self.readInput())
        else:
            self.menuSetControler(self.readInput())


    # Function is controller which is based on the userInput. 
    # Based on the input  function invokes specific methodsh
    def menuPirntControler(self, userInput):
        os.system("clear")
        if userInput == CONST.SHOP_OPTION:
            self.__shop.printOptions()
            self.__shop.printController(self.readInput())
            return True
        elif (userInput == CONST.CLINET_OPTION):
            self.__client.printOptions()
            self.__client.printControler(self.readInput())
            return True 
        elif (userInput == CONST.PRINT_SET_SETTINGS):
            self.printAllSettings()
            return True
        else:
            return False
            
    # Settings controller which invokes the set for relevant class 
    def menuSetControler(self, userInput):
        if (userInput == CONST.SHOP_OPTION):
            self.getShop().printOptions()
            self.getShop().setController(self.readInput())
            return True
        elif (userInput == CONST.CLINET_OPTION):
            self.__client.printOptions()
            self.__client.setController(self.readInput())
            return True
        elif (userInput == CONST.PRINT_SET_SETTINGS):
            self.setAllAettings()
            return True
        else:
            print("Invalid input")
            return False
    
    # Function invokes pritns settings of shop and one of the clinets (most of them will be the same so their is no
    # point in poluting the screen with clinet data)
    def printAllSettings(self):
        if (isinstance(self.__shop, Shop)):
            print("----- SHOP SETTINGS -----")
            self.__shop.printSettings()
        if (isinstance(self.__client, Client)):
            print("----- CLINET SETTINGS -----")
            self.__client.printCustomerSettings()
    
    def setAllAettings(self):
        if (isinstance(self.__shop, Shop)):
            print("----- SHOP SETTINGS -----")
            self.__shop.setSettings()
        if (isinstance(self.__client, Client)):
            print("----- CLIENT SETTINGS -----")
            self.__client.setSettings()

    # Methods read user data provided by the user and converts it into integer
    def readInput(self):
        tmp = input("> ")
        try:
            number = int(tmp)
            return  number
        except(ValueError, TypeError):
            return 0
    
    # Function clears terminal
    def clearTerminal(self):
        print("Press any key...")
        input()
        os.system("clear")

# GETTERS                    
    def getShop(self):
        return self.__shop


        
        
