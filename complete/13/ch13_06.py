# class Vehicle:
#     def __init__(self, maker, model, year):
#         self.maker = maker
#         self.model = model
#         self.year = year
    
#     def start(self):
#         return "engine start()"

#     def stop(self):
#         return "engine stop()"
    
# class Sedan(Vehicle):
#     def __init__(self, maker, model, year, doors):
#         super().__init__(maker,model,year)
#         self.doors = doors
    
#     def open_doors(self):
#         return "open doors"

# class Truck(Vehicle):
#     def __init__(self, maker, model, year, capacity):
#         super().__init__(maker,model,year)
#         self.capacity = capacity
    
#     def load_cargo(self, weight):
#         if weight <= self.capacity:
#             return "Cargo loaded"
#         else:
#             return "Exceed capacity"
        

# # Sedan 객체
# my_sedan = Sedan("Mazda", "roadster", 2018, 2)
# print(f"maker => {my_sedan.maker}, model => {my_sedan.model}, year => {my_sedan.year}, doors => {my_sedan.doors}")
# print(f"{my_sedan.start()}")
# print(f"{my_sedan.open_doors()}")
# # Truck 객체
# my_truck = Truck("Ford", "F-150", 2019, 10000)
# print(f"maker => {my_truck.maker}, model => {my_truck.model}, year => {my_truck.year}, capacity => {my_truck.capacity}")
# print(f"{my_truck.start()}")
# print(f"{my_truck.load_cargo(5000)}")
# print(f"{my_truck.load_cargo(15000)}")

class Student:
    def __init__(self, name, id, math, sci, eng):
        self.name = name
        self.id = id
        self.math = math
        self.sci = sci
        self.eng = eng
    
    def get_name(self):
        return self.name

    def total(self):
        return self.math + self.sci + self.eng

    def avg(self):
        return self.total() / 3
    
class Teacher:
    def __init__(self, name, id, subject):
        self.name = name
        self.id = id
        self.subject= subject
    
    def get_name(self):
        return self.name

    def set_students(self, students):
        self.students = students

    def subject_total(self):
        total = 0
        for s in self.students:
            if self.subject == '수학':
                total += s.math
            elif self.subject == '과학':
                total += s.sci
            elif self.subject == '영어':
                total += s.eng
        return total

    def subject_avg(self):
        return self.subject_total() / len(self.students)
    

s1 = Student("민지", "240901",80, 75, 60)
s2 = Student("하니", "240902",100, 55, 80)
s3 = Student("다니엘", "240903",90, 45, 90)
s4 = Student("해린", "240904",80, 100, 55)
s5 = Student("혜인", "240905",88, 75, 36)

print(s1.avg())
print(s2.avg())
print(s3.avg())
print(s4.avg())
print(s5.avg())

t1 = Teacher("민희진", "051001", "수학")
t2 = Teacher("방시혁", "051002", "과학")
t3 = Teacher("이수만", "051003", "영어")

t1.set_students([s1,s2,s3,s4,s5])
t2.set_students([s1,s2,s3,s4,s5])
t3.set_students([s1,s2,s3,s4,s5])

print(t1.subject_avg())
print(t2.subject_avg())
print(t3.subject_avg())
