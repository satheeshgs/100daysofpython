def add(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add(576,829,192,223))


def calculate(n, **kwargs): #keyword arguments
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.max_speed = kwargs.get("speed")
        self.type = kwargs.get("type")

my_car = Car(make="Honda", model="Jazz", color="Red Pearl")

print(my_car.make)