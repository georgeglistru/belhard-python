class Phone:
    brand: str
    model: str
    issue_year: int

    def __init__(self, br, m, y):
        self.brand = br
        self.model = m
        self.issue_year = y

    def receive_call(self, caller):
        print(f"Звонит {caller}")

    def get_info(self):
        return (self.brand, self.model, self.issue_year)

    def __str__(self):
        return f"""{{
Бренд: {self.brand}         
Модель: {self.model}         
Год выпуска: {self.issue_year}         
}}
"""

ph1 = Phone("Samsung", "A52", 2020)
print(ph1)

ph1.receive_call("+375 12 123 45 65")

print(ph1.get_info())
