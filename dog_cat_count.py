def cat_dog(k):
    cat = k.count("cat")
    dog = k.count("dog")
    if dog == cat:
        return True
    else:
        return False
    
k = input("Enter String-->")
cat_dog(k)