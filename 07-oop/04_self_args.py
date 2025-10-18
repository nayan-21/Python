class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))

# print(Chaicup.describe())  # This will raise TypeError because no instance is passed
print(cup.describe())  # This will work fine as instance is passed implicitly
print(cup_two.describe())  # This will also work fine as instance is passed implicitly
print(Chaicup.describe(cup))  # This will also work fine as instance is passed explicitly
print(Chaicup.describe(cup_two))  # This will also work fine as instance is passed explicitly
# print(cup.size)