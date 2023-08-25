class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed  # km/h

    def __str__(self):
        return f"{self.brand} {self.model}. {self.year} year of manufacture. Current speed {self.speed} km/h."

    def accelerate(self):
        self.speed = self.speed + 5
        return f"Accelerating by 5 km/h. Current speed {self.speed} km/h."

    def brake(self):
        self.speed = self.speed - 5
        return f"Braking by 5 km/h. Current speed {self.speed} km/h."
