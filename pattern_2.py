user = int(input("Enter star value->"))

for i in range(1,user+1,2):
    print("*"*i)
for i in range(user-2,0,-2):
    print("*"*i)
