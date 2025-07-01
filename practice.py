class Student:
    def __init__(self, name, clas, age):
        self.name = name
        self.clas = clas
        self.age = age

student1 = Student("Vyan Agarwal", "4G", 9)
student2 = Student("Mahi Agarwal", "6C", 12)
print(student2.clas)

class Cars:
    def __init__(self, model, company, color):
        self.model = model
        self.company = company
        self.color = color
    def printInfo(self):
        print(self.model)        
        print(self.color)
        print(self.company)
    
car1 = Cars("RX350", "Lexus", "Silver")
car1.printInfo()