class students:
    name = ""
    roll_number = ""
    age = ""
    marks = ""
    def __init__(self):
        self.name = input("Studens Name:-->")
        self.roll_number = input("Studens Roll Number:-->")
    def setAge(self):
        self.age= input("Enter Age -->")
    def setMarks(self):
        self.marks = input("Enter Marks")
    def display(self):
        print(self.name,self.roll_number,self.age,self.marks)
        
    
s1 = students()
s1.setAge()
s1.setMarks()
s1.display()