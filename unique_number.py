for i in range(1000,10000):
    i = str(i)
    if float(i[0]) == float(int(i[-1])/2):
        if float(i[:2]) ==  float(int(i[2:])/2):
            if i[1] == i[2]:
                print(i)