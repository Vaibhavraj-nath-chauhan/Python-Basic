import datetime
now = datetime.datetime.now()
today = datetime.date.today()
print(today,"\n")
print(now)

print("\nSetting Time")
new = today + datetime.timedelta(90)
print(new)
