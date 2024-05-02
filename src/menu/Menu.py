from .MenuConsts import MenuConsts as menuConsts
from ..settings.Settings import Setting  
import os

class Menu:
    # Consturctor of main class which instalizes the variables of class
    def __init__(self):
        self.settings = Setting.__new__(Setting) 
        self.option = 0
        self.shouldExit= False;

    # Method runs the main menu till shouldExit variable of object is changed to True
    def mainMenuRunner(self):
        while not self.shouldExit:
            self.printMainMenu()
            isInputValid = False
            while not isInputValid: 
                isInputValid = self.setOption(self.readInput())
            self.mainMenuControler()
            self.clearTerminal()

    # Print main menu with options
    def printMainMenu(self):
        print("Main menu of shop simulation")
        print("1 Print options for simulation") 
        print("2 Set options of simulations")
        print("3 Print chart from the simulation")
        print("4 Print results")
        print("5 Save to file")
        print("6 Exit application")
        print("Enter number related to the option")

    # Controler of main menu, who based on the option invokes next operations
    def mainMenuControler(self):
        if menuConsts.printSimulationSettings == self.getOption() or menuConsts.setSimulationSettings == self.getOption():
            self.simulationSettings(self.getOption())
        elif menuConsts.printChart == self.getOption():
            self.printChart()
        elif menuConsts.printResults == self.getOption():
            self.printResults()
        elif menuConsts.saveToFile == self.getOption():
            self.saveToFile()
        elif menuConsts.exitApp== self.getOption():
            self.exitApp() 

    # Function opens the menu with settings of simulation
    def simulationSettings(self, actionType):
        self.clearTerminal()
        self.settings.settingMenuRunner(actionType)
        return
    # Function prints charts of simulation 
    def printChart(self):
        print("Print char")
        return
    # Functions prints the result of simulations
    def printResults(self):
        print("Print results")
        return
    # Functions saves files and charts of simulation in memory storage
    def saveToFile(self):
        print("Save file");
        return 
    # Function exits the application 
    def exitApp(self):
        self.shouldExit= True
        return 

    # Method takes input from the user and tries to convert it to number. In case of exception method returns 0
    def readInput(self):
        tmp = input("> ")
        try:
            number = int(tmp)
            return  number
        except(ValueError, TypeError):
            print("Option must be a number")
            return 0

    # Functions clears terminal after any key was pressed
    def clearTerminal(self):
        input("Press any key...")
        os.system('clear')
        

# GETTERS AND SETTERS
    def getOption(self):
        return self.option
    def getSetting(self):
        return self.settings

    # Setter on booster with returned result of setting
    def setOption(self, option):
        if ( menuConsts.mainMenuLowerBounderie <= option and menuConsts.mainMenuHigherBounderie >= option):
            self.option = option
            return True
        return False
 
        
