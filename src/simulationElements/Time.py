class Time:
    def __init__(self):
        self.current_time = 6  # Sklep otwiera się o 6:00

    def advance(self):
        self.current_time += 1  # Przejdź do następnej godziny

    def is_open(self):
        return 6 <= self.current_time < 22  # Sklep jest otwarty od 6:00 do 22:00
