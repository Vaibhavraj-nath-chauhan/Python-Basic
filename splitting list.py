with open("testing.txt" ,"r") as f:
    all_data = f.read()
    all_data= all_data.split("\n")

lis = [i.split(":") for i in all_data]
print(lis)