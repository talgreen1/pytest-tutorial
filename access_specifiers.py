# Public -> member_name
# Protected -> _member_name
# Private -> __member_name

class Car:
    number_of_wheels = 4
    _color = 'black'
    __year = "2017" # Actual name is _Car__year

class BMW(Car):
    def __init__(self):
        print(f'Protected attribute: Color: {self._color}')



car = Car()
print(f'Public attributes: number of wheel: {car.number_of_wheels}')
bmw = BMW()
print(car._Car__year)