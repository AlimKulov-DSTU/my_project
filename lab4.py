#Базовый класс Transport
class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def move(self):
        print(f"Transport is moving at {self.speed} km/h")
    
    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}"

#Дочерний класс Car
class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats
    
    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")
    
    def honk(self):
        print("Beep beep!")
    
    def __str__(self):
        return f"Car: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"
    
    def __len__(self):
        return self.seats
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
    
    def __add__(self, other):
        if isinstance(other, (Car, Bike)):
            return self.speed + other.speed
        return NotImplemented

#Дочерний класс Bike
class Bike(Transport):
    def __init__(self, brand, speed, type_bike):
        super().__init__(brand, speed)
        self.type_bike = type_bike
    
    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")
    
    def __str__(self):
        return f"Bike: {self.brand}, Speed: {self.speed}, Type: {self.type_bike}"

#Практика использования
def main():
    #Создание объектов
    transport = Transport("TEST", 100)
    car1 = Car("Chaika", 160, 7)
    car2 = Car("Volga", 147, 5)
    car3 = Car("Moskvich", 120, 5)
    bike1 = Bike("Misnk", 20, "dirt")
    bike2 = Bike("Ural", 20, "mountain")
    #Вывод объектов
    print(transport)
    print(car1)
    print(car2)
    print(car3)
    print(bike1)
    print(bike2)
    
    #Проверка методов
    print("\nМетод move:")
    transport.move()
    car2.move()
    bike1.move()
    
    print("\nМетод honk:")
    car3.honk()
    
    #Проверка len
    print("\nМест в car2:", len(car2))
    
    #Сравнение машин
    print("\nСравнение car1 == car3:", car1 == car3)
    
    #Сложение скоростей
    print("\nСкорость car1 + car2:", car1 + car2)
    print("Скорость car1 + bike2:", car1 + bike2)
    
    #Дополнительное задание
    print("\nВызов move() для всех объектов:")
    spisok = [transport, car1, car2, car3, bike1, bike2]
    for x in spisok:
        x.move()

if __name__ == "__main__":
    main()