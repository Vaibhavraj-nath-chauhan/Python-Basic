i = int(input("Enter Length of list-->"))
i = [int(input(f"Enter Numer {j+1}-->")) for j in range(i)]
if len(i)==1:
    print(i[0])
else:
    print(list(set(i))[-2])