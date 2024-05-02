from .ElementsConst import ElementsConst as  CONST
import random
class Client: 
    def __init__(self):
        self.__shopingTime = CONST.DEF_SHOPING_TIME
        self.__averageCartCost = CONST.DEF_AVG_CART_COST
        self.actual_cart_cost = random.normalvariate(self.__averageCartCost,10) # Na podstawie średniej wartości wyznacza losową liczbę, 10 to odchylenie std
        self.__shopingTimeAbounde = CONST.DEF_SHOPING_TIME_ABOUNDE
        self.printClinetOptions()

     
    def printClinetOptions(self):
        for i in range(len(CONST.CLINET_OPTIONS)): 
            print(i+1, CONST.CLINET_OPTIONS[i])
        return
     
    # Metoda zwraca wydane pieniądze, 
    def get_spent_money(self):
        #....Logika umożliwiając znalezienie(lub nie znalezienie) poszukiwanych towarów
        return self.actual_cart_cost
        
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


