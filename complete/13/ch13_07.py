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
        

# Sedan 객체
my_sedan = Sedan("Mazda", "roadster", 2018, 2)
print(f"maker => {my_sedan.maker}, model => {my_sedan.model}, year => {my_sedan.year}, doors => {my_sedan.doors}")
print(f"{my_sedan.start()}")
print(f"{my_sedan.start_engine()}")






