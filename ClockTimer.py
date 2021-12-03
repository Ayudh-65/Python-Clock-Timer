import time
import winsound

x = 0
currentTime = time.strftime("%H:%M:%S")

print("Current Time is:", currentTime)
addTime = float(input("Set a timer for how many minutes?:"))

currentTimeInt = float(time.strftime("%H%M%S"))
timerEnd = (currentTimeInt + (addTime*100))

print("Timer set for", addTime, "minutes.")

while(int(time.strftime("%H%M%S")) < timerEnd):
    time.sleep(1)

print("Your", addTime, "minutes are over!")
winsound.PlaySound("Beeping.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
x=input("Press enter to stop the timer...")
