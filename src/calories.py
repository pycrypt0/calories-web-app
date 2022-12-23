from src.temperature import Temperature


class Calorie:
    """Represent amount of calories calculated with
    BMR = 10 * weight + 6.25 * height - 5 * age - 10 * temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.age = age

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 * self.age - self.temperature * 10
        return result


if __name__ == "__main__":
    temperature = Temperature(country="italy", city="rome").get()
    calorie = Calorie(temperature=temperature, weight=85, height=190, age=24)
    print(calorie.calculate())
