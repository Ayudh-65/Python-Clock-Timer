import time

currentTime = time.strftime("%H:%M:%S")

print("Current Time is:", currentTime)
addTime = int(input("Set a timer for how many minutes?:"))

currentTimeInt = int(time.strftime("%H%M%S"))
timerEnd = (currentTimeInt + (addTime*100))

print("Timer set for", addTime, "minutes!")

while(True):
    if(int(time.strftime("%H%M%S")) >= timerEnd):
        print("BEEP BEEP! Your", addTime, "minutes are over.")
        break