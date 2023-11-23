class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self.__coordinates = coordinates
        self.__speed = speed
        self.__brand = brand
        self.__year = year
        self.__number = number

    def __str__(self):
        return (f"Coordinates = {self.__coordinates}, Speed = {self.__speed}, Brand = {self.__brand}, "
                f"Year = {self.__year}, Number = {self.__number}")

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        x, y = self.coordinates
        if pos_y <= y <= pos_y + width and pos_x <= x <= pos_x + length:
            return True
        return False

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value):
        if len(value) != 2:
            raise ValueError()
        self.__coordinates = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError()
        self.__speed = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) and len(brand) != 0:
            raise ValueError()
        self.__brand = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value < 1900:
            raise ValueError()
        self.__year = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if value < 0:
            raise ValueError()
        self.__number = value


class Passenger:
    def __init__(self, passengers_capacity, number_of_passengers):
        self.__passengers_capacity = passengers_capacity
        self.__number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, value):
        if value <= 0:
            raise ValueError()
        self.__passengers_capacity = value

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, value):
        if value < 0:
            raise ValueError()
        self.__number_of_passengers = value


class Cargo:
    def __init__(self, carrying):
        self.__carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, value):
        if value < 0:
            raise ValueError()
        self.__carrying = value


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError()
        self.__height = value


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number, color):
        super().__init__(coordinates, speed, brand, year, number)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if not isinstance(value, str) and len(color) == 0:
            raise ValueError()
        self.__color = value

    @property
    def mileage(self):
        return self._mileage


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, name, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.__name = name
        self.__port = port

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError()

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        if isinstance(value, str):
            self.__port = value
        else:
            raise ValueError()


class Car(Auto):
    pass


class Bus(Auto, Passenger):
    pass


class CargoAuto(Auto, Cargo):
    pass


class Boat(Ship):
    pass


class PassengerShip(Ship, Passenger):
    pass


class CargoShip(Ship, Cargo):
    pass


class Seaplane(Plane, Ship):
    pass


a = Transport((2, 3), 2, 5, 15, 6256)
print(a.__str__())
a.speed = -3
