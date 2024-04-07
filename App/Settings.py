class Setting:
    def __init__(self):
        self.__shopType = "DEAFULT VALUE" 
    def getShopType(self):
        return self.__shopType
    def setShopType(self, shopType):
        if (shopType == "self-service"):
            self.__shopType = "self-service"
        elif (shopType == "mixed"):
            self.__shopType = "mixed"
        elif (shopType == "cashier-service"):
            self.__shopType = "cashier-service"
        else:
            print("Shop type not supported")
