class ProfitCalculator:
    def __init__(self, shop):
        self.shop = shop
        self.daily_sales = 0
        self.daily_costs = 0
        self.daily_loss = 0

    def calculate_daily_sales(self):
        return self.daily_sales
    def calculate_daily_costs(self, num_days,employees):
        employee_costs = sum(employee.salary for employee in employees) / 30 * num_days
        goods_costs = self.daily_sales * (1 - self.shop.profit_margin)
        self.daily_costs = employee_costs + goods_costs
        return self.daily_costs
    def calculate_daily_loss(self):
        return self.daily_loss
        
    #Metoda dodająca podany profit do profitu dziennego
    def add_profit(self, sales):
        profit = sales * self.shop.profit_margin
        cost = sales * (1 - self.shop.profit_margin)
        self.daily_sales += profit
        self.daily_costs += cost

