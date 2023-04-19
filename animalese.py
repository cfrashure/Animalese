from playsound import playsound
from time import sleep
import os
from pathlib import Path

# Enable the below line for a shell clear on mac/linux/unix
os.system('clear')
# Enable the below line for a cmd clear on windows
# os.system('cls')
msg = ""
while msg != "exit":
    msg = input("Enter your animalese message, or type \"exit\" to end the program. ").lower()
    if msg == "exit":
        break
    for char in msg:
        if char == " ":
            sleep(0.05)
        elif char == ",":
            sleep(0.1)
        elif char == "." or char == "!" or char == "?":
            sleep(0.3)
        else:
            playsound("%s/sounds/%s.mp3" % (Path(__file__).parent, char))
