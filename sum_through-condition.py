def lone_sum(k):
    if 13 in k:
        find = k.index(13)
        return sum(k[:find])
    else:
        return sum(k)
    
k = [int(input(f"Enter Value {i+1}-->")) for i in range(3)]
print("Sum is:-->",lone_sum(k))