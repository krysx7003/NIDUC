from .ElementsConst import ElementsConst as CONST
class Shop:
    def __init__(self) -> None:
        self.__shopValue = CONST.DEF_SHOP_VALUE
        self.__shopType = CONST.DEF_SHOP_TYPE
        self.__regularCheckoutsNumber = CONST.DEF_REGULAR_CHECKOUTS_NUMBER
        self.__selfServiceCheckoutsNumber = CONST.DEF_SELF_SERVICE_CHECKOUTS_NUMBER
        self.__workerNumber = CONST.DEF_WORKER_NUMBER
        self.__timeOfProductPlacment = CONST.DEF_TIME_OF_PRODUCT_PLACMENT

    def printClinetOptions(self):
        for i in range(len(CONST.SHOP_OPTIONS)): 
            print(i+1, CONST.CLINET_OPTIONS[i])
        return 

    # GETTERS
    def getShopSize(self):
        return self.__shopValue
    def getShopType(self):
        return self.__shopType
    def getRegularCheckoutsNumber(self):
        return self.__regularCheckoutsNumber
    def getSelfServiceCheckoutsNumber(self):
        return self.__selfServiceCheckoutsNumber
    def getWorkerNumber(self):
        return self.__workerNumber
    def getTimeOfProductPlacment(self):
        return self.__timeOfProductPlacment

    # SETTERS
    def setShopSize(self,shopValue):
        if (shopValue > 0):
            self.__shopValue = shopValue
    def setShopType(self, shopType):
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
    def setTimeOfProductPlacment(self, productPlacmentTime):
        if (productPlacmentTime > 0):
            self.__timeOfProductPlacment = productPlacmentTime



