class Queue:
    def __init__(self):
        self.clients = []

    def add_customer(self, customer):
        self.clients.append(customer)

    def remove_customer(self):
        return self.clients.pop(0) if self.clients else None

    def get_length(self):
        return len(self.clients)
