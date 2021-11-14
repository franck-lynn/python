from  car.Car import Car

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    def describe_battery(self):
        return "this car has a " + str(self.battery_size) + "-KWH battery." 


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(
    my_tesla.get_descriptive_name()
)
print(
    my_tesla.describe_battery()
)
