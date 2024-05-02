from .ElementsConst import ElementsConst as  CONST
import random
class Client: 
    # Consturcotr of client class
    def __init__(self):
        self.__shopingTime = CONST.DEF_SHOPING_TIME
        self.__averageCartCost = CONST.DEF_AVG_CART_COST
        self.actual_cart_cost = random.normalvariate(self.__averageCartCost,10) # Na podstawie średniej wartości wyznacza losową liczbę, 10 to odchylenie std
        self.__shopingTimeAbounde = CONST.DEF_SHOPING_TIME_ABOUNDE
        self.__numberOfCilents = CONST.DEF_NUMBER_OF_CLIENTS

    # Function prints the option for client class
    def printOptions(self):
        print("Choose client variable to print/set")
        for i in range(len(CONST.CLINET_OPTIONS)): 
            print(i+1, CONST.CLINET_OPTIONS[i])
        print("Enter relevant number: ")
    
    def printControler(self, usrInput):
        if (usrInput == CONST.SHOPING_TIME):
            print("Current shoping time: ",self.getShopingTime()) 
        elif (usrInput == CONST.CART_VALUE):
            print("Current average cart value: ", self.getAverageCartCost())
        elif (usrInput == CONST.ABOUNDE_TIME):
            print("Current time after which clients will leave the shop: ", self.getShopingTimeAbounde())
        elif (usrInput == CONST.CLIENT_NUM):
            print("Current number of clients: ", self.getNumberOfClients())
        elif (usrInput == CONST.ALL_CLIENT):
                self.printClientSettings() 

    def setController(self, usrInput):
        if (usrInput == CONST.SHOPING_TIME):
            print("Enter shoping time: ")
            self.setShopingTime(self.readInput())
        elif (usrInput == CONST.CART_VALUE):
            print("Enter average cost of shpoing: ")
            self.setAverageCartCost(self.readInput())
        elif (usrInput == CONST.ABOUNDE_TIME):
            print("Enter time after which the client wil leave the shop: ")
            self.setShopingTimeAbounde(self.readInput())
        elif (usrInput == CONST.CLIENT_NUM):
            print("Enter number of clients: ")
            self.setNumberOfCielnts(self.readInput())
        elif (usrInput == CONST.ALL_CLIENT):
            self.setSettings()

        

    # Można obie te funkcje spróbować przy wykorzystaniu zmieniej połaczyć z pojeczyńczym ustawianiem zmienne

    # Function prints current settings for client
    def printClientSettings(self): 
        print("Shoping time: ", self.getShopingTime())
        print("Average cost of shoping cart: ", self.getAverageCartCost())
        print("Shpoing time abounde: ", self.getShopingTimeAbounde())
        print("Number of clients: ", self.getNumberOfClients())

    # Function sets all of the client fileds by user
    def setSettings(self):
        print("WARTNING! In case of incorrect input data value of field will remain as deafult")
        print("Enter shoping time: ")
        self.setShopingTime(self.readInput())
        print("Enter average cost of shoping cart: ")
        self.setAverageCartCost(self.readInput())
        print("Enter time after clinet will aboundon shop: ")
        self.setShopingTimeAbounde(self.readInput())
        print("Enter number of clients: ")
        self.setNumberOfCielnts(self.readInput())
    
    def readInput(self):
        tmp = input("> ")
        try:
            number = int(tmp)
            return  number
        except(ValueError, TypeError):
            return 0


    # GETTERS
    def getShopingTime(self):
        return self.__shopingTime
    def getAverageCartCost(self):
        return self.__averageCartCost
    def getShopingTimeAbounde(self):
        return self.__shopingTimeAbounde
    def getNumberOfClients(self):
        return self.__numberOfCilents
        

    # SETTERS
    def setShopingTime(self, shopingTime):
        if ( shopingTime > 0):
            self.__shopingTime = shopingTime
    def setAverageCartCost(self, avgCartCost) :
        if ( avgCartCost > 0):
            self.__averageCartCost= avgCartCost 
    def setShopingTimeAbounde(self, abounde):
        if ( abounde > 0):
            self.__shopingTimeAbounde = abounde 
    def setNumberOfCielnts(self, numberOfClients):
        if (numberOfClients > 0):
            self.__numberOfCilents = numberOfClients 


