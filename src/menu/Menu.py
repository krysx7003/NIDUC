from .MenuConsts import MenuConsts as menuConsts
from ..settings.Settings import Setting
from ..simulationElements import Shop, ProfitCalculator,  Queue
from ..simulationElements.Time import Time
from ..simulationElements.Queue import Queue
from ..simulationElements.Client import Client
from ..simulationElements.Shop import Shop
from ..simulationElements.Employee import Employee
from ..simulationElements.ProfitCalculator import ProfitCalculator

import random
import numpy as np

class Menu:
    def __init__(self):
        self.settings = Setting()
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

    def run_shift(self, shift):
        # Ustaw czas początku i końca zmiany
        start_time, end_time = (6, 14) if shift == 1 else (14, 22)

        # Przetwarzanie klientów dla każdej godziny zmiany
        for hour in range(start_time, end_time):
            self.time.current_time = hour
            customers_this_hour = self.generate_customers()
            for customer in customers_this_hour:
                self.queue.add_customer(customer)
                self.process_customers_queue()

    def generate_customers(self):
        # Generowanie klientów z krzywej gaussa, z najwyższym punktem około godziny 15
        mean = 15 - self.time.current_time  # przesunięcie średniej
        num_customers = int(abs(np.random.normal(mean, 1)) * 10)  # przykładowe wartości
        return [Client() for _ in range(num_customers)]

    def process_customers_queue(self):
        # Przetwarzanie kolejki klientów
        while not self.queue.is_empty() and self.shop.is_open():
            for employee in self.employees:
                if employee.is_on_shift(self.time.current_time):
                    # Obsłuż klientów, zakładając, że każdy pracownik może obsłużyć około 3 klientów na minutę
                    customers_to_process = min(self.queue.get_length(), employee.process_customers(1))
                    for _ in range(customers_to_process):
                        customer = self.queue.remove_customer()
                        self.profit_calculator.add_profit(customer.get_spent_money())
                    # Sprawdź, czy klienci nie oczekiwali zbyt długo
                    self.queue.remove_long_waiting_customers(30)  # 30 minut

    # Metoda sprawdzająca, czy klasa jest pusta (potrzebna dla procesowania kolejki)
    def is_empty(self):
        return len(self.clients) == 0

    # Metoda do usuwania klientów czekających zbyt długo
    def remove_long_waiting_customers(self, max_waiting_time):
        # Usuń klientów, którzy czekają dłużej niż max_waiting_time
        self.clients = [customer for customer in self.clients if customer.waiting_time < max_waiting_time]
        # Potencjalnie utracony zysk dla tych, którzy odeszli
        self.potential_profit_lost += sum(customer.spent_money for customer in self.clients if customer.waiting_time >= max_waiting_time)
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
 
        
