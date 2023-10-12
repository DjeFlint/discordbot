class Car:
    def __init__(self, color, mileage):
            self.color = color
            self.mileage = mileage

    def __str__(self):
        return f"{self.color} car has {self.mileage} in total!"

bluecar = Car("Blue", "20,000")
redcar = Car("Red", "30,000")

print(bluecar)
print(redcar)