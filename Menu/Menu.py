import sys
sys.path.append('/media/ciamcio/SandDisk/NiDUC/Project/NIDUC_PROJ/')
from MenuConsts import *
from App.Settings import * 

class Menu:
    def __init__(self):
        settings = Setting() 
        self.option = 0
        self.printMainMenu() 

    def printMainMenu(self):
        print("Main menu of shop simulation")
        print("1. Set options for simulation") 
        print("2. Print chart from the simulation")
        print("3. Print results")
        print("4. Save to file")
        print("Enter number related to the option")
        self.inputController(MenuConsts.mainMenuLowerBounderie, MenuConsts.mainMenuHigherBounderie)
        self.mainMenuControler()

    def inputController(self, lowerLimit, higherLimit):
        while True:
            self.inputFromUser()
            if self.checkInput(lowerLimit, higherLimit):
                return

    def inputFromUser(self):
        tmp = input(">")
        self.setOption(tmp)

    def checkInput(self, lowerLimit, higherLimit):
        if lowerLimit > self.getOption() and higherLimit < self.getOption(): 
            return False 
        else:
           return True 

    def mainMenuControler(self):
        if MenuConsts.simulationSettings == self.getOption():
            self.simulationSettings()
        elif MenuConsts.printChart == self.getOption():
            self.printChart()
        elif MenuConsts.printResults == self.getOption():
            self.printResults()
        else:
            self.saveToFile()

    def simulationSettings(self):
        # Let's begin with the number of checkOuts and types of checko
        return
    def printChart(self):
        return
    def printResults(self):
        return
    def saveToFile(self):
        return 
    def getOption(self):
        return self.option
    def setOption(self, option):
        self.option = option
 
        
