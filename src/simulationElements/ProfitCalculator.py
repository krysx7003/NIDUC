class ProfitCalculator:
    def __init__(self, shop):
        self.shop = shop
        self.daily_profit = 0
        self.daily_loss = 0

    def calculate_daily_profit(self):
        # ... Logika do obliczania dziennego zysku i potencjalnego zysku
        return self.daily_profit
    def calculate_daily_loss(self):
        # ... Logika do obliczania dziennego zysku i potencjalnego zysku
        return self.daily_loss
        
    #Metoda dodająca podany profit do profitu dziennego
    def add_profit(self,profit):
        self.daily_profit += profit

    def add_loss(self,profit_lost):
        self.daily_loss += profit_lost     