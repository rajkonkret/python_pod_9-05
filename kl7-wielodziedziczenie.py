class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Jadę pojazdem")


class Car(Vehicle):
    def drive(self):
        print("Jadę samochodem")


class Bike(Vehicle):
    def drive(self):
        print("Jadę rowerem")


class HybridCar(Car, Bike):
    def drive(self):
        print("Jade samochodem hybrydowym")


car1 = Car("Toyota")
car1.drive()
row = Bike("Giant")
row.drive()

hyb = HybridCar("Honda")
hyb.drive()


# 13:10