from ..simulationElements import *
class Setting:
    __SETTINGS_MAIN_MENU = ["Shop settings", "Client settings", "Current settings", "Back"]
    def __init__(self):
        self.__listOfClients = []
        self.__shop = None

    def printOptionMenu(self): 
        for i in range(len(Setting.__SETTINGS_MAIN_MENU)):
            print(i+1, Setting.__SETTINGS_MAIN_MENU[i])
        return
