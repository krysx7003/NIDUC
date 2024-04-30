class Queue:
    def __init__(self):
        self.clients = []
        self.profit_lost = 0

    def add_client(self, client):
        self.clients.append(client)

    def remove_client(self,remove_id):
        return self.clients.pop(remove_id) if self.clients else None

    def is_empty(self):
        return len(self.clients) == 0
    
    def tick_time(self,time_amount):
        for _ in range(len(self.clients)):
            self.clients[_].increase_time_waited(time_amount)

    # Metoda która wyszukuje kilentów którzy czekali zbyt długo a następnie ich usuwa
    def remove_long_waiting_clients(self,long_time):
        self.profit_lost = 0
        for _ in range(len(self.clients)):
            if(self.clients[_].time_in_queue()>=long_time):
                # Pieniądze które kilent mógł wydać zostają dodane do strat
                self.profit_lost += self.clients[_].get_spent_money()
                self.remove_client(_)
    
    # GETTERS
    def get_length(self):
        return len(self.clients)
    def get_profit_lost(self):
        return self.profit_lost