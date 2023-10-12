class Cat:
    species = "Oriental Shorthair"
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

Odin = Cat("Odin", 3, "Grijs/Beige")
Ragnar = Cat("Ragnar", 3, "Zwart")

print(Odin.color, Ragnar.age)
print(Odin.species)