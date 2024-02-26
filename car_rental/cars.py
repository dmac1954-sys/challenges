class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.rented = False

        
    def rent_car(self):
        self.rented = True

    def return_car(self):
        self.rented = False
        
    def __repr__(self):
        if self.rented:
            rented_status = "Rented"
        else:
            rented_status = "Available"

        return f"The car is {self.make} {self.model} from {self.year}. Status: {rented_status}"
    
class CarRental:
    def __init__(self):
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)

    def print_inventory(self):
        print("Car Inventory:")
        for car in self.inventory:
            print(car)

def main():

    car1 = Car("Ford", "Focus", 2022)
    car2 = Car("VW", "Golf", 2023)

    rental = CarRental()
    rental.add_car(car1)
    rental.add_car(car2)

    car1.return_car()
    rental.print_inventory()

if __name__ == "__main__":
    main()

    

    