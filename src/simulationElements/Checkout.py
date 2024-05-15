class Checkout:
    def __init__(self, efficiency):
        self.efficiency = efficiency

    def process_customers(self, minutes):
        # Zwraca liczbę klientów obsłużonych w danym czasie
        return minutes * self.efficiency


class RegularCheckout(Checkout):
    def __init__(self):
        # Regularna kasa obsługuje średnio 3 klientów na minutę
        super().__init__(efficiency=3)


class SelfCheckout(Checkout):
    def __init__(self):
        # Kasa samoobsługowa obsługuje średnio 4 klientów na minutę
        super().__init__(efficiency=4)

    def get_efficency(self):
        return self.efficiency
