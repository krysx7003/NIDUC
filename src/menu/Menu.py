from .MenuConsts import MenuConsts as menuConsts
from ..settings.Settings import Setting
from ..simulationElements.Time import Time
from ..simulationElements.Queue import Queue
from ..simulationElements.Client import Client
from ..simulationElements.Shop import Shop
from ..simulationElements.Employee import Employee
from ..simulationElements.ProfitCalculator import ProfitCalculator
import os
import random
import numpy as np

class Menu:
    def __init__(self):
        self.settings = Setting.__new__(Setting) 
        self.shop = None
        self.time = Time()
        self.profit_calculator = None
        self.queue = Queue()
        self.employees = []
        self.option = 0
        self.shouldExit = False

    # ... [inne metody klasy]

    def simulate_day(self):
        # Losowanie sklepu zgodnie z poleceniem 1.
        self.shop = self.create_random_shop()

        # Symulacja zmian zgodnie z poleceniem 2.
        for shift in range(1, 3):
            self.run_shift(shift)

        # Podsumowanie dnia
        self.profit_calculator = ProfitCalculator(self.shop)
        self.profit_calculator.calculate_daily_profit()

    def create_random_shop(self):
        # Losuj liczbę pracowników, kas normalnych i samoobsługowych
        num_employees = random.randint(1, 10)  # przykładowy zakres
        num_regular_checkouts = random.randint(1, 5)
        num_self_service_checkouts = random.randint(1, 5)

        # Tworzenie pracowników
        self.employees = [Employee(i, f'Pracownik_{i}') for i in range(num_employees)]

        # Tworzenie sklepu
        shop = Shop()
        shop.setWorkerNumber(num_employees)
        shop.setRegularCheckoutsNumber(num_regular_checkouts)
        shop.setSelfServiceCheckoutsNumber(num_self_service_checkouts)
        return shop

    # Metody run_shift,generate_customers,process_customers_queue odwołują się do kilentów jako customers w reszcie programu są to clients trzeba to znormalizować
    def run_shift(self, shift):
        # Ustaw czas początku i końca zmiany
        start_time, end_time = (6, 14) if shift == 1 else (14, 22)
        # Przetwarzanie klientów dla każdej godziny zmiany
        for employee in self.employees:
            employee.start_shift(start_time)
        for hour in range(start_time, end_time):
            self.time.current_time = hour
            clients_this_hour = self.generate_clients()
            for client in clients_this_hour:
                #Ten kod dodaje tylko pojedyńczego klienta 
                self.queue.add_client(client)
                self.process_clients_queue()

    def generate_clients(self):
        # Generowanie klientów z krzywej gaussa, z najwyższym punktem około godziny 15
        mean = 15 - self.time.current_time  # przesunięcie średniej
        num_clients = int(abs(np.random.normal(mean, 1)) * 10)  # przykładowe wartości
        return [Client() for _ in range(num_clients)]

    def process_clients_queue(self):
        # Przetwarzanie kolejki klientów
        while not self.queue.is_empty() and self.shop.is_open(self.time):
            for employee in self.employees:
                if employee.is_on_shift(self.time.current_time):
                    # Obsłuż klientów, zakładając, że każdy pracownik może obsłużyć około 3 klientów na minutę
                    clients_to_process = min(self.queue.get_length(), employee.process_clients(1))
                    for _ in range(clients_to_process):
                        client = self.queue.remove_client(0)
                        #'NoneType' object has no attribute 'add_profit' nie ogarniam czemu tak się dzieje
                        self.profit_calculator.add_profit(client.get_spent_money())
                    # Zwiększ czas który czekali klienci w kolejce
                    self.queue.tick_time(1) # 1 minuta
                    # Sprawdź, czy klienci nie oczekiwali zbyt długo
                    self.queue.remove_long_waiting_clients(30)  # 30 minut
                    # Dodaj pieniądze które mogli wydać nie obsłużeni kilenci jako stracone zyski
                    self.profit_calculator.add_potentials_profit(self.queue.get_profit_lost())

    # Method runs the main menu till shouldExit variable of object is changed to True
    def mainMenuRunner(self):
        while not self.shouldExit:
            self.printMainMenu()
            isInputValid = False
            while not isInputValid: 
                isInputValid = self.setOption(self.readInput())
            self.mainMenuControler()
            self.clearTerminal()

    def simmulationRunner(self):
        print("How long should simmulation run")
        daysToRun = self.readInput()
        currentDay = 1
        for currentDay in range(1,daysToRun):
            self.simulate_day()

    # Print main menu with options
    def printMainMenu(self):
        print("Main menu of shop simulation")
        print("1 Print options for simulation") 
        print("2 Set options of simulations")
        print("3 Print chart from the simulation")
        print("4 Print results")
        print("5 Save to file")
        print("6 Run simulation")
        print("7 Exit application")
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
        elif menuConsts.runSim== self.getOption():
            self.startSimulation()
        elif menuConsts.exitApp== self.getOption():
            self.exitApp() 

    # Function opens the menu with settings of simulation
    def simulationSettings(self, actionType):
        self.clearTerminal()
        self.settings.settingMenuRunner(actionType)
        return
    # Function prints charts of simulation 
    def printChart(self):
        print("Print chart")
        return
    # Functions prints the result of simulations
    def printResults(self):
        print("Print results")
        return
    # Functions saves files and charts of simulation in memory storage
    def saveToFile(self):
        print("Save file")
        return 
    def startSimulation(self):
        self.simmulationRunner()
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
        
    # Checks if the input of user which is an argument is correct value from the range of numbers
    def handleInput(self, input, lowerLimit, higherLimit):
        if lowerLimit.value > int(input) or higherLimit.value < int(input):
            return False 
        else:
           return True 


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
 
        
