from win32api import GetAsyncKeyState as KeyState
from win32con import VK_SPACE as SPACE
from win32gui import GetWindowText as GetText
from win32gui import GetForegroundWindow as GetCurrentWindow
from pyautogui import scroll as scroll_mouse
from ctypes import windll as windows_dll
from os import system as cmd_run
from colorama import init as colorama_init
from colorama import Fore as fore
from colorama import Back as back
from colorama import Style as style
from time import sleep as time_sleep


scroll = 100000
game_window = 'Counter-Strike: Global Offensive'
bunny_hop_key = SPACE
wait_game_interval = 3000


windows_dll.kernel32.SetConsoleTitleW('Pixelsuft Python Bhop Script (bhop.py)')
cmd_run('color 0a')


def print_logo():
    colorama_init(autoreset=True)
    print('''
00000  0    0 000000 000000    000000 0    0
0    0 0    0 0    0 0    0    0    0  0  0
00000  000000 0    0 000000    000000   00
0    0 0    0 0    0 0         0        0
00000  0    0 000000 0      0  0       0'''[1:].replace('0', f'{fore.BLACK}{back.GREEN} {style.RESET_ALL}'), end='')


def mainloop():
    if game_window:
        while True:
            if GetText(GetCurrentWindow()) == game_window:
                if KeyState(bunny_hop_key):
                    scroll_mouse(-scroll)
            else:
                time_sleep(wait_game_interval / 1000)
    else:
        while True:
            if KeyState(bunny_hop_key):
                scroll_mouse(-scroll)


if __name__ == '__main__':
    print_logo()
    del SPACE
    del windows_dll
    del colorama_init
    del fore
    del back
    del style
    mainloop()
