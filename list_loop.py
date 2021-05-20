email_up = []
while True:
    count = 0
    email = input("Enter Your Email Address: ")
    email_up.append(email)
    for i in email:
        if i.isdigit():
            count+=int(i)
    print(count)
    if len(email_up)==5:
        break
