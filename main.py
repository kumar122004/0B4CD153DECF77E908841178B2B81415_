import calendar
yr=int(input("enter year"))
if calendar.isleap(yr):
  print(yr,"is a leap year")
else:
  print(yr,"is a not leap year")
