import time

currentTime = time.strftime("%H:%M:%S")

print("Current Time is:", currentTime)
addTime = float(input("Set a timer for how many minutes?:"))

currentTimeInt = float(time.strftime("%H%M%S"))
timerEnd = (currentTimeInt + (addTime*100) - 1)

print("Timer set for", addTime, "minutes!")

while(int(time.strftime("%H%M%S")) < timerEnd):
    time.sleep(1)

print("Your", addTime, "minutes are over!")
x=input()
