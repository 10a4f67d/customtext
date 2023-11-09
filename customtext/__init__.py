import time
import os, platform
from pystyle import Center

class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

def animate(text, color, speed):
    # USAGE:
    # intro("Animated text lmao", colors.RED, 0.1)
    #  1^           2^                   3^   4^
    # 1 : Function
    # 2 : Text
    # 3 : Color
    # 4 : Time
    length = len(text)

    for i in range(length):
        colored_text = color + text[:i+1] + colors.RESET
        print(colored_text)
        time.sleep(speed)
        
        if i < length - 1:
            print("\033[F\033[K", end="")

def intro(Banner, color, speed):
    # USAGE:
    # Banner = """Ascii art lmao"""
    # intro(Banner, colors.RED, 0.1)
    #  1^    2^            3^   4^
    # 1 : Function
    # 2 : Ascii Art
    # 3 : Color
    # 4 : Time
    length = len(Banner)

    for i in range(length):
        colored_text = color + Banner[:i+1] + colors.RESET
        print(colored_text)
        time.sleep(speed)
        
        if i < length - 1:
            if platform.system() == "Windows":
                os.system('cls')
            else:
                os.system('clear')
            print("\033[F\033[K", end="")