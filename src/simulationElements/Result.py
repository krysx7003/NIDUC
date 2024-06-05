# Class contains the results of a simulation which was runned previously
class Result:

    # Consturctor of a Result class which initialization of variables 
    def __init__(self):
        self.__profit = []
        self.__loss = []
        self.__satisfactionScore = 0
        self.__processedClients = 0
        self.__lostClients = 0

    # Method updates satisfaction level for customers which were handled. A arguemnt passed to the method is the satisfaction level of customer during checkout. 
    def updatedSatisfactionScore(self, satisfactionLevel):
        self.__satisfactionScore += satisfactionLevel
        self.__processedClients += 1
    
    # Method updated number of lsot clients during simulation
    def updatedLostClients(self, lostClients):
        if (lostClients >= 1):
            self.__lostClients += lostClients

    # Method calculates avreage satisfaction level for all the clients who has left shop
    def calculateAvgSatisfactionLevel(self):
        return int(self.__satisfactionScore/(self.__processedClients+self.__lostClients))

    # GETTERS

    def getProfit(self):
        return self.__profit
    def getLoss(self):
        return self.__loss
    def getSatisfactionScore(self):
        return int(self.__satisfactionScore)
    def getProccessedClients(self):
        return int(self.__processedClients)
    def getLostClients(self):
        return int(self.__lostClients)

    # SETTERS 

    def setProfit(self, profit):
        self.__profit = profit 
    def setLoss(self, loss):
        self.__loss = loss
    def setSatisfactionScore(self, satisfactionScore):
        self.__satisfactionScore = satisfactionScore
    def setProccessedClients(self, proccessedClients):
        self.__processedClients = proccessedClients
    def setLostClients(self, lostClients):
        self.__lostClients = lostClients
