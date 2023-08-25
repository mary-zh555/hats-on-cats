class Country:
    def __init__(self, name: str, population: int) -> None:
        self.name = name
        self.population = population

    def add(self, other) -> "Country":
        if type(other) != Country:
            raise TypeError("other must be a Country instance")

        name_union: str = self.name + " " + other.name
        population_sum: int = self.population + other.population
        return Country(name_union, population_sum)

    def __add__(self, other) -> "Country":
        if type(other) != Country:
            raise TypeError("other must be a Country instance")

        name_union: str = self.name + " " + other.name
        population_sum: int = self.population + other.population
        return Country(name_union, population_sum)
