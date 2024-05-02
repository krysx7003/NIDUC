class ProfitCalculator:
    def __init__(self, shop):
        self.shop = shop
        self.daily_profit = 0
        self.potential_profit_lost = 0

    def calculate_daily_profit(self):
        # ... Logika do obliczania dziennego zysku i potencjalnego zysku


        pass
    #Metoda dodająca podany profit do profitu dziennego
    def add_profit(self,profit):
        self.daily_profit += profit

    def add_potentials_profit(self,profit_lost):
        self.potential_profit_lost += profit_lost     