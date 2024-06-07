class ProfitCalculator:
    def __init__(self, shop):
        self.shop = shop
        self.daily_profit = 0
        self.daily_loss = 0
        self.potential_daily_lose =  0
        self.potential_profit_lost: int  = 0

    def calculate_daily_profit(self):
        # ... Logika do obliczania dziennego zysku i potencjalnego zysku
        return self.daily_profit
    def calculate_daily_loss(self):
        # ... Logika do obliczania dziennego zysku i potencjalnego zysku
        return self.daily_loss
        
    # Method adds the profit to dailyt_profit
    def add_profit(self,profit):
        self.daily_profit += profit

    # Method adds loos to the the amount that was lost already
    def add_lost(self,profit_lost):
        self.daily_loss += profit_lost     
    
    # Method returns potential profit loss
    def get_potential_profit_lost(self):
        return self.potential_profit_lost
