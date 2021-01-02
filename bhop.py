# Turn off bind to jump on space!
bind=None
scroll=10000000



while True:
    try:
        from win32api import GetAsyncKeyState as key_state
        from win32con import VK_SPACE as is_space
        from pyautogui import scroll as scroll_mouse
        from pyautogui import press as press_key
        from ctypes import windll as win_dll
        from os import system as cmd_run

        win_dll.kernel32.SetConsoleTitleW('Pixelsuft Python Bhop Script (bhop.py)')
        cmd_run('color 0a')
        
        print('bhop.py started!')
        while True:
            if key_state(is_space):
                
                if bind==None:
                    scroll_mouse(-scroll)
                else:
                    press_key(str(bind))
    except KeyboardInterrupt:
        print('\nCtrl+C Pressed\n')