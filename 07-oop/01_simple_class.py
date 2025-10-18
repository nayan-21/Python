class Nayan:
    pass
class Manan:
    pass

print(type(Nayan()))
print(type(Manan()))
print(type(Nayan))  

UNayan = Nayan()
print(type(UNayan))
print(type(UNayan) is Nayan)
print(type(UNayan) is Manan)
print(isinstance(UNayan, Nayan))
print(isinstance(UNayan, Manan))
print(isinstance(UNayan, object))
print(isinstance(Nayan, object))
