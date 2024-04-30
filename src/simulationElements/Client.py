from .ElementsConst import ElementsConst as  CONST
class Client: 
    def __init__(self):
        self.__shopingTime = CONST.DEF_SHOPING_TIME
        self.__averageCartCost = CONST.DEF_AVG_CART_COST
        self.__shopingTimeAbounde = CONST.DEF_SHOPING_TIME_ABOUNDE
        self.printClinetOptions()

     
    def printClinetOptions(self):
        for i in range(len(CONST.CLINET_OPTIONS)): 
            print(i+1, CONST.CLINET_OPTIONS[i])
        return 

    # GETTERS
    def getShopingTime(self):
        return self.__shopingTime
    def getAverageCartCost(self):
        return self.__averageCartCost
    def getShopingTimeAbounde(self):
        return self.__shopingTimeAbounde

    # SETTERS
    def setShopingTime(self, shopingTime):
        if ( shopingTime > 0):
            self.__shopingTime = shopingTime
        return 
    def setAverageCartCost(self, avgCartCost) :
        if ( avgCartCost > 0):
            self.__averageCartCost= avgCartCost 
        return 
    def setShopingTimeAbounde(self, abounde):
        if ( abounde > 0):
            self.__shopingTime = abounde 
        return 


