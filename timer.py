import time
import keyboard
import threading

paused = False
stopped = False
def timer(seconds):
    global paused, stopped
    while seconds > 0 and not stopped:
        if not paused:
            #print("\r", end="")
            minutes_left = seconds // 60
            seconds_left = seconds % 60
            print(f"\r{minutes_left:02d}:{seconds_left:02d}", end="")
            time.sleep(1)
            seconds -= 1
    if stopped:
        print("\nTimer is stopped.")
    else:
        print("\nTime us up!")

def keyboard_input():
    global paused, stopped
    while True:
        if keyboard.is_pressed('p') and not paused:
            paused = True
            print("\nTimer is paused, press 'r' to resume.")
        elif keyboard.is_pressed('r') and paused:
            paused = False
            print("\rResuming Timer...")
        elif keyboard.is_pressed('s'):
            stopped = True
            break
        time.sleep(0.1) # Preventing high CPU usage

print("Press 'p' to pause, 'r' to resume and 's' to stop the timer." )

print("Here you must declare the time you want for the Timer!")

minutes = int(input("Minutes: "))
if minutes < 0 or minutes > 1440:
    raise ValueError("Minutes must be between 0 and 1440.")

seconds = int(input("Seconds: "))
if seconds < 0 or seconds > 59:
    raise ValueError("Seconds must be between 0 and 59.")

total_seconds = minutes * 60 + seconds

timer_thread = threading.Thread(target=timer, args=(total_seconds,))
keyboard_thread = threading.Thread(target=keyboard_input)

timer_thread.start()
keyboard_thread.start()

timer_thread.join()
keyboard_thread.join()
