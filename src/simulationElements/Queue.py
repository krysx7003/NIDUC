from src.simulationElements.Customer import Client


class Queue:
    
    # Constructor of a queue
    def __init__(self):
        self.clients = []
        self.profit_lost = 0
        self.__satisfactionScore = 0
        self.__processedClientsNumber = 0

    # Method adds customer to the virtual queuej 
    def add_customer(self, client):
        self.clients.append(client)

    # Method removes the customer of specified indecks from the list
    def remove_customer(self,remove_id):
        if self.clients:
            return  self.clients.pop(remove_id)
        else: 
            return None

    # Method checks if queue is empty. Based on that returns the result
    def is_empty(self):
        return len(self.clients) == 0
    
    # Method iterates over the client list which are curentlly in the queue and incraese time waited by them 
    def tick_time(self,time_amount):
        for _ in range(len(self.clients)):
            self.clients[_].increase_time_waited(time_amount)


    # Metoda która wyszukuje kilentów którzy czekali zbyt długo a następnie ich usuwa
    def remove_long_waiting_customers(self,long_time):
        self.profit_lost = 0
        i = 0
        removedClients = 0
        while i < len(self.clients)-1:
            if(self.clients[i].time_in_queue()>=long_time):
                # Pieniądze które kilent mógł wydać zostają dodane do strat
                self.profit_lost += self.clients[i].get_spent_money()
                self.remove_customer(i)
                removedClients += 1
            i += 1
        return int(removedClients)


    # Method iterates over the clients which are curentlly in the queue and decrease their satisfaction level by one 
    def descreseClientsSatisfactionLevel(self):
        for _ in range(len(self.clients)):
            self.clients[_].setSatisfactionLevel(self.clients[_].getSatisfactionLevel() - 1)
   

    # GETTERS
    def get_length(self):
        return len(self.clients)
    def get_loss(self):
        return self.profit_lost
    def getSatisfactionScore(self):
        return self.__satisfactionScore
    def getPorcessedClientsNumber(self):
        return self.__processedClientsNumber
