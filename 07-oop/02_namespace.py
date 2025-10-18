class Chai:
    origin = "India"
    is_hot = False
    
print(Chai.origin)  # Output: India
print(Chai.is_hot)  # Output: False
print(type(Chai))    # Output: <class 'type'>
print(type(Chai.origin))  # Output: <class 'str'>
print(Chai)

Chai.is_hot = True
print(Chai.is_hot)  # Output: True
# print(Chai.__dict__)  # Output: class namespace dictionary

Nayan = Chai()
print(Nayan.origin)  # Output: India
print(Nayan.is_hot)  # Output: True 

Nayan.is_hot = False
Nayan.origin = "Nepal"
print(Nayan.origin)  # Output: Nepal
print(Nayan.is_hot)  # Output: False
print(Chai.is_hot)   # Output: True

print(Nayan.__dict__)  # Output: instance namespace dictionary