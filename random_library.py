from random import randint

Rn = randint(10,20)

isTrue = False

for i in range(3):
    user_in = int(input("Enter Your input: "))
    if user_in > Rn:
        print("pred is > original number")
    elif user_in < Rn:
        print("pred is < original number")
    elif user_in==Rn:
        print("pred == original number")
        isTrue = True
        break
if isTrue:
    print("You predicited true")