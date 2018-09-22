import datetime

print("Hello~")
BDY = input("Birthday:year")
BDM = input("Birthday:month")
BDD = input("Birthday:date")
today = datetime.date.today().year

print(str(today - int(BDY)) + " years old")
Month = datetime.date(int(BDY), int(BDM),int(BDD)).month  - datetime.date.today().month

if Month <= 0:
    Month = Month + 12

print(str(Month))
