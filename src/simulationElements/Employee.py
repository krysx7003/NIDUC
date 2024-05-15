import datetime
from .ElementsConst import ElementsConst as CONST

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.efficiency = CONST.DEF_SERVED_CLIENTS_PER_MINUTE  # ilość obsłużonych klientów na minutę
        self.on_shift = False
        self.shift_start = None
        self.shift_end = None
        self.shift_length = CONST.DEF_TIME_ON_SHIFT
        self.salary = CONST.DEF_AVG_EMPLOYEE_SALARY  # stałe wynagrodzenie miesięczne dla pracownika

    def start_shift(self, start_time):
        if self.on_shift:
            raise ValueError(f"Pracownik {self.name} ({self.employee_id}) jest już na zmianie.")
        self.on_shift = True
        self.shift_start = start_time
        self.shift_end = start_time+self.shift_length

    def end_shift(self, end_time):
        if not self.on_shift:
            raise ValueError(f"Pracownik {self.name} ({self.employee_id}) nie jest aktualnie na zmianie.")
        self.on_shift = False
        self.shift_end = end_time
        # Zwróć czas pracy dla obliczeń płacowych
        return self.shift_end - self.shift_start

    def is_on_shift(self, check_time):
        # Sprawdź czy pracownik jest na zmianie w podanym czasie
        return self.shift_start <= check_time <= self.shift_end

    def get_paid(self):
        return  self.salary

    def process_customers(self, minutes):
        # Zwraca liczbę klientów obsłużonych w danym czasie
        return self.efficiency * minutes

    def report_performance(self):
        # Generuj raport o wydajności pracownika
        if self.on_shift:
            worked_time = datetime.datetime.now() - self.shift_start
        else:
            worked_time = self.shift_end - self.shift_start if self.shift_end else datetime.timedelta()
        processed_clients = self.process_customers(worked_time.total_seconds() / 60)
        return f"Pracownik {self.name} ({self.employee_id}) obsłużył {processed_clients} klientów."
