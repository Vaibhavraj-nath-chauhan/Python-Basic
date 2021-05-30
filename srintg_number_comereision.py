x = "my123name323islots119"
y = ""
lis = []
for i in range(len(x)):
     if x[i].isdigit():
        y+=x[i]
        try:
            if x[i+1].isalpha():
                    lis.append(int(y))
                    y=""
        except:
            lis.append(int(y)) 
print(sorted(lis)[-1])
         