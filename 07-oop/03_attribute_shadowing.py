class Chai:
    temperature = "hot"
    strength = "Strong"


cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ",cutting.temperature)
print("cup size is  ",cutting.cup)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
del cutting.cup
print(cutting.temperature)
# print(cutting.cup) # This will raise an AttributeError since 'cup' attribute is deleted from instance

