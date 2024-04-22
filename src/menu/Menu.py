from .MenuConsts import MenuConsts as menuConsts
from ..settings.Settings import Setting  

class Menu:
    # Consturctor of main class which instalizes the variables of class
    def __init__(self):
        settings = Setting() 
        self.option = 0
        self.shouldExit= False;

    # Method runs the main menu till shouldExit variable of object is changed to True
    def mainMenuRunner(self):
        while not self.shouldExit:
            self.printMainMenu()
            self.setOption(self.inputController(menuConsts.mainMenuLowerBounderie, menuConsts.mainMenuHigherBounderie))
            self.mainMenuControler()

    # Print main menu with options
    def printMainMenu(self):
        print("Main menu of shop simulation")
        print("1. Set options for simulation") 
        print("2. Print chart from the simulation")
        print("3. Print results")
        print("4. Save to file")
        print("5. Exit application")
        print("Enter number related to the option")

    # Method controles and validates the input from the user
    def inputController(self, lowerLimit, higherLimit):
        isInputCorrect = False  
        tmp = 0
        while not isInputCorrect:
            tmp = self.inputFromUser()
            isInputCorrect = self.handleInput(tmp, lowerLimit, higherLimit)  
        return int(tmp) 
                 

    # Method takes input from the user and tries to convert it to number. In case of exception method returns 0
    def inputFromUser(self):
        tmp = input("> ")
        try:
            number = int(tmp)
            return  number
        except(ValueError, TypeError):
            print("Option must be a number")
            return 0

    # Checks if the input of user which is an argument is correct value from the range of numbers
    def handleInput(self, input, lowerLimit, higherLimit):
        if lowerLimit.value > int(input) or higherLimit.value < int(input):
            return False 
        else:
           return True 

    # Controler of main menu, who based on the option invokes next operations
    def mainMenuControler(self):
        if menuConsts.simulationSettings.value == self.getOption():
            self.simulationSettings()
        elif menuConsts.printChart.value == self.getOption():
            self.printChart()
        elif menuConsts.printResults.value == self.getOption():
            self.printResults()
        elif menuConsts.saveToFile.value == self.getOption():
            self.saveToFile()
        elif menuConsts.exitApp.value == self.getOption():
            self.exitApp() 

    def simulationSettings(self):
        print("Simulation setting")
        return
    def printChart(self):
        print("Print char")
        return
    def printResults(self):
        print("Print results")
        return
    def saveToFile(self):
        print("Save file");
        return 
    def exitApp(self):
        self.shouldExit= True
        return 

# GETTERS AND SETTERS
    def getOption(self):
        return self.option
    def setOption(self, option):
        self.option = option
 
        
