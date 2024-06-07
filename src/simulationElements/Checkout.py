class Checkout:
    def __init__(self, efficiency):
        self.efficiency = efficiency

    # Method returns the number of clients processed by the employee
    def process_customers(self, minutes):
        return minutes * self.efficiency


# Class representing regular checkout which efficiency equals to 3
class RegularCheckout(Checkout):
    def __init__(self):
        super().__init__(efficiency=3)


# Class representing selfcheckout which efficiency equals to 4
class SelfCheckout(Checkout):
    def __init__(self):
        super().__init__(efficiency=4)

    # Function returns the efficiency of checkout
    def get_efficency(self):
        return self.efficiency
