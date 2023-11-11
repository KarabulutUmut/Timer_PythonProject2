import time
import keyboard

def timer(seconds):
    paused = False
    while seconds > 0:
        if not paused:
            print("\r", end="")
            minutes_left = seconds // 60
            seconds_left = seconds % 60
            print(f"{minutes_left:02d}:{seconds_left:02d}", end="")
            time.sleep(1)
            seconds -= 1
        if keyboard.is_pressed('p'):
            paused = True
            print("\nTimer is paused, press 'r' to resume.")
            while paused:
                if keyboard.is_pressed('r'):
                    paused = False
                    print("\rResuming Timer...")
        if keyboard.is_pressed('s'):
            print("\nTimer is stopped.")
            break
    else:
        print("\nTime us up!")


print("Press 'p' to pause, 'r' to resume and 's' to stop the timer." )

print("Here you must declare the time you want for the Timer!")

minutes = int(input("Minutes: "))
if minutes < 0 or minutes > 1440:
    raise ValueError("Minutes must be between 0 and 1440.")

seconds = int(input("Seconds: "))
if seconds < 0 or seconds > 59:
    raise ValueError("Seconds must be between 0 and 59.")

total_seconds = minutes * 60 + seconds
timer(total_seconds)


