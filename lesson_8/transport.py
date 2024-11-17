from abc import ABC, abstractmethod


class Transport(ABC):
    brand: str
    model: str
    issue_year: int
    color: str
    mileage: int

    def __init__(self, brand, model, issue_year, color):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color
        self.mileage = 0

    @abstractmethod
    def move(self, num_km):
        if num_km <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        self.mileage += num_km


class Car(Transport):
    engine_type: str

    def __init__(self, brand, model, issue_year, color, engine_type):
        super().__init__(brand, model, issue_year, color)
        self.engine_type = engine_type

    def move(self, num_km):
        super().move(num_km)
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) проехала {self.mileage} километров"

class Airplane(Transport):
    lifting_capacity: int

    def __init__(self, brand, model, issue_year, color, lifting_capacity):
        super().__init__(brand, model, issue_year, color)
        self.lifting_capacity = lifting_capacity

    def move(self, num_km):
        super().move(num_km)
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) пролетел {self.mileage} километров"


car = Car("Tesla", "X1", 2020, "Черная", "Электро")
print(car.move(100))
# print(car.move(-100))
print(car.move(2000))
print(car.move(3100))

boeng = Airplane("Boeng", "A100", 2015, "Белый", 1010)
print(boeng.move(1000))
# print(boeng.move(-1000))
print(boeng.move(2000))
print(boeng.move(3100))
