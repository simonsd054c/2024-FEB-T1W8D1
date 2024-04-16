# class

class Car:
    # constructor
    def __init__(self, _color, _make):
        self._color = _color
        self._make = _make

    # Getters - Accessors
    def get_color(self):
        return self._color
    
    def get_make(self):
        return self._make
    
    # Setters - Mutators
    def set_color(self, _color):
        self._color = _color

    def run(self):
        print(f"{self._make} is running!! Vrrooom Vrrrrooomm!!!")


# Create an object of the class 'Car'
my_car = Car("White", "Honda")

my_car.set_color("Red")

print(my_car.get_color())
print(my_car.get_make())
my_car.run()


your_car = Car("Black", "Toyota")
print(your_car.get_color())
your_car.run()


class PetrolCar(Car):
    def __init__(self, _color, _make, _capacity_of_tank):
        super().__init__(_color, _make)
        self._capacity_of_tank = _capacity_of_tank

    def get_capacity(self):
        return self._capacity_of_tank
    

my_petrol_car = PetrolCar("Silver", "BMW", 50)
my_petrol_car.run()
print(my_petrol_car.get_capacity())


class ElectricCar(Car):
    # pass
    # Overriding
    def run(self):
        print("I run silently!! No Vroooming!!")


my_electric_car = ElectricCar("Yellow", "Hyundai")
my_electric_car.run()