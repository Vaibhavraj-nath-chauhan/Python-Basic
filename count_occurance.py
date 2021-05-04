user = input("String-->")
k = [i for i in user]
my_set = list(set(k))
for i in my_set:
    print(i,k.count(i))