def my_speed(speed,day = False):
    if day:
        speed -= 5
    if speed <= 60:
        print("No tickect")
    elif speed >61 or speed<80:
        print("Small ticket")
    elif speed > 81:
        print("Biggest Ticket")
        
day = input("Your Bday or not (True/False) -->")
speed = int(input("Speed-->"))
my_speed(speed,day)