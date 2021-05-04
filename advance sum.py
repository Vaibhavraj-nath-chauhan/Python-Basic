def lone_sum(a,b,c):
    if a == b == c:
        return 0
    elif a==b:
        return c
    elif a==c:
        return b
    elif b == c:
        return a
    else:
        return a+b+c

a = int(input("Enter Value of A -> "))
b = int(input("Enter Value of B -> "))
c = int(input("Enter Value of C -> "))

print("Sum is:-->",lone_sum(a,b,c))