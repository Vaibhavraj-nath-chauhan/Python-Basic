def alaram_clock(i,end=False):
    if i<7:
        if end:
            if i==6:
                return "OFF"
            else:
                return "10:00"
        else:
            if i==6:
                return "10:00"
            else:
                return "07:00"
    else:
        return "Not a Valid Number"
i = int(input("Enter Day--> "))
end = input("Its a weekend or not (True/Flase)")
alaram_clock(i,end)