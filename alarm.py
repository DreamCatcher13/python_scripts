#from playsound import playsound # pip install playsound==1.2.2
import time
import os
os.system("") # for ansi escape to work on Windows but doesn't on win7 :(

# escape chars will manipulate the terminal
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"  #return cursor to home position

def alarm(seconds):
	time_elapsed = 0
	
	print(CLEAR)
	while time_elapsed < seconds:
		time.sleep(1)
		time_elapsed += 1
		
		time_left = seconds - time_elapsed
		minutes_left = time_left // 60 # integer division
		seconds_left = time_left % 60
		
		#print(f"\rAlarm will sound in: {minutes_left:02d}:{seconds_left:02d}",end="") # formatting digits
		print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
		
	#playsound("alarm.mp3")
	
min = int(input("How many minutes to wait: "))
sec = int(input("How many secons to wait: "))

alarm(min*60+sec)
		
