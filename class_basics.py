class windows_user:
    Ram = "8GB"
    SSD = "128GB"
    name = "Windows Microsoft"
    
    #creating a constructor 
    def __init__(self):
        self.name = input("Your name-->")
        

    def details(self):
        print("Ram -->",self.Ram,"SSD -->",self.SSD,"User Name -->" ,self.name)

user1 = windows_user()
user1.details()

user2 = windows_user()
user2.details()