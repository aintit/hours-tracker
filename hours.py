from datetime import date
import os

if not os.path.exists("hours.txt"):
    open("hours.txt", "w").close()

hoursfile = open("hours.txt")
hourstext = hoursfile.read()
hoursfile.close()
hoursnow = raw_input("How many hours did you work today? ")
hoursarray = hourstext.splitlines()

today = date.today()
todaystr = today.isoformat()

if len(hoursarray) == 0:
    hoursarray.append(todaystr + " " + hoursnow)
elif hoursarray[-1].find(todaystr) != -1:
    hoursarray[-1] = todaystr + " " + hoursnow
else:
    hoursarray.append(todaystr + " " + hoursnow)

hourstext2 = "\n".join(hoursarray)
hoursfile = open("hours.txt", "w")
hoursfile.write(hourstext2)
hoursfile.close()
