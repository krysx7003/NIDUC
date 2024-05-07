from .ElementsConst import ElementsConst as CONST
class Shop:
    # Constructor of shop class
    def __init__(self) -> None:
        self.__shopValue = CONST.DEF_SHOP_VALUE
        self.__shopType = CONST.DEF_SHOP_TYPE
        self.__regularCheckoutsNumber = CONST.DEF_REGULAR_CHECKOUTS_NUMBER
        self.__selfServiceCheckoutsNumber = CONST.DEF_SELF_SERVICE_CHECKOUTS_NUMBER
        self.__workerNumber = CONST.DEF_WORKER_NUMBER
        self.__timeOfProductPlacment = CONST.DEF_TIME_OF_PRODUCT_PLACMENT
        self.__rushHour = CONST.DEF_RUSH_HOURS

    # Functions prints the options for the shop class
    def printOptions(self):
        print("Choose variable to print/set")
        for i in range(len(CONST.SHOP_OPTIONS)): 
            print(i+1 , CONST.SHOP_OPTIONS[i])
        print("Enter relevant number: ")

    # Prints currennt settings of shop
    def printController(self, input):
        if (input == CONST.VALUE):
            print("Current shop size: ", self.getSize()) 
        elif (input == CONST.TYPE):
            print("Current shop type: ", self.getType()) 
        elif (input == CONST.REG_CHECKOUTS):
            print("Current number of regular checkouts: ", self.getRegularCheckoutsNumber())
        elif (input == CONST.SS_CHECKOUTS):
            print("Current number of self-service checkuots: ", self.getSelfServiceCheckoutsNumber())
        elif (input == CONST.WORKER):
            print("Current number of workers: ", self.getWorkerNumber())
        elif (input == CONST.TIME_OF_PRODUCT_PLACMENT):
            print("Current time of product placemnt: ", self.getTimeOfProductPlacment())
        elif (input == CONST.RUSH_HOUR):
            print("Current rush hour: ", self.getRushHour())
        elif (input == CONST.ALL_SHOP):
            self.printSettings()

    # Metoda zwraca prawdę jeżeli current_time jest z zakresu <6,22>(włącznie)
    def is_open(self, time):
        return time.current_time<=22 & time.current_time>=6
    
    # Method sets the option for the shop (only one setting)
    def setController(self, userInput):
        if (userInput== CONST.VALUE):
            print("Enter shop's size: ")
            self.setSize(self.readInput())
        elif (userInput== CONST.TYPE):
            print("Enter shop type: ")
            self.setType(input("> "))
        elif (userInput== CONST.REG_CHECKOUTS):
            print("Enter number of regular checkouts: ")
            self.setRegularCheckoutsNumber(self.readInput())
        elif (userInput== CONST.SS_CHECKOUTS):
            print("Enter number of self-service checkouts: ")
            self.setSelfServiceCheckoutsNumber(self.readInput())
        elif (userInput== CONST.WORKER):
            print("Enter number of shop workers: ")
            self.setWorkerNumber(self.readInput())
        elif (userInput== CONST.TIME_OF_PRODUCT_PLACMENT):
            print("Enter time of product placment: ")
            self.setTimeOfProductPlacment(self.readInput())
        elif (userInput== CONST.RUSH_HOUR):
            print("Enter a rush hour: ")
            self.setRushHour(self.readInput())
        elif (userInput== CONST.ALL_SHOP):
            self.setSettings() 
        
        


    # Function prints current shop settings
    def printSettings(self):
        print("Shop size: ", self.getSize())
        print("Shop type: ", self.getType())
        print("Number of regualr checkouts: ", self.getRegularCheckoutsNumber())
        print("Number of self-service checkouts: ", self.getSelfServiceCheckoutsNumber())
        print("Number of workers: ", self.getWorkerNumber())
        print("Time of product placment: ", self.getTimeOfProductPlacment())
        print("Rush hour: ", self.getRushHour())

    # Function sets all the settings for the shop simulation
    def setSettings(self):
        print("WARTNING! In case of incorrect input data value of field will remain as deafult")
        print("Enter shop's size: ")
        self.setSize(self.readInput())
        print("Enter shop type: ")
        self.setType(input("> "))
        print("Enter number of regular checkouts: ")
        self.setRegularCheckoutsNumber(self.readInput())
        print("Enter number of self-service checkouts: ")
        self.setSelfServiceCheckoutsNumber(self.readInput())
        print("Enter number of workers: ")
        self.setWorkerNumber(self.readInput())
        print("Enter time of product placement: ")
        self.setTimeOfProductPlacment(self.readInput())
        print("Enter rush hour for the shop: ")
        self.setRushHour(self.readInput())

    # Method read input from user
    def readInput(self):
        tmp = input("> ")
        try:
            number = int(tmp)
            return  number
        except(ValueError, TypeError):
            return 0

    # GETTERS
    def getSize(self):
        return self.__shopValue
    def getType(self):
        return self.__shopType
    def getRegularCheckoutsNumber(self):
        return self.__regularCheckoutsNumber
    def getSelfServiceCheckoutsNumber(self):
        return self.__selfServiceCheckoutsNumber
    def getWorkerNumber(self):
        return self.__workerNumber
    def getTimeOfProductPlacment(self):
        return self.__timeOfProductPlacment
    def getRushHour(self):
        return self.__rushHour

    # SETTERS
    def setSize(self,shopValue):
        if (shopValue > 0):
            self.__shopValue = shopValue
    def setType(self, shopType):
        if (shopType == "large"):
            self.__shopType = shopType 
        elif (shopType == "medium"):
            self.__shopType = shopType
        else:
            self.__shopType = CONST.DEF_SHOP_TYPE
    def setRegularCheckoutsNumber(self, checkoutNum): 
        if (checkoutNum >= 1):
            self.__regularCheckoutsNumber = checkoutNum
    def setSelfServiceCheckoutsNumber(self, checkoutNum):
        if (checkoutNum >= 1):  
            self.__selfServiceCheckoutsNumber = checkoutNum
    def setWorkerNumber(self, workerNum):
        if (workerNum >= 1):
            self.__workerNumber = workerNum
    def setTimeOfProductPlacment(self, time):
        if (time >= 0):
            self.__timeOfProductPlacment =  time
    def setRushHour(self, rushHour):
        if (rushHour >= 0 and rushHour <= 24):
            self.__rushHour = rushHour



