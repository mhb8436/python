class Vehicle:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
    
    def start(self):
        return "engine start()"

    def stop(self):
        return "engine stop()"
    
class Sedan(Vehicle):
    def __init__(self, maker, model, year, doors):
        super().__init__(maker,model,year)
        self.doors = doors
    
    def open_doors(self):
        return "open doors"
    
    def start_engine(self):
        super().start()
        return "Sedan start engine"

class Truck(Vehicle):
    def __init__(self, maker, model, year, capacity):
        super().__init__(maker,model,year)
        self.capacity = capacity
    
    def load_cargo(self, weight):
        if weight <= self.capacity:
            return "Cargo loaded"
        else:
            return "Exceed capacity"
    
    def start(self):
        return "truck start"
        

# Truck 객체
my_truck = Truck("Ford", "F-150", 2019, 10000)
print(f"maker => {my_truck.maker}, model => {my_truck.model}, 
      year => {my_truck.year}, capacity => {my_truck.capacity}")
print(f"{my_truck.start()}")





