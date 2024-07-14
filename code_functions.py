import os
from datetime import datetime
import time
import pyautogui

DESKTOP_PATH = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

def get_datetime(**args) -> str:
    """
    Gets current system date and time.
    
    Parameters:
        None
    Returns:
        string: current datetime
    """

    curr_datetime = datetime.now().strftime("%d %B, %Y %A, %I:%M %p")
    return curr_datetime

def open_apps(app_name: str) -> None:
    """
    Opens the given apps.

    Parameters:
        string: app name
    Returns:
        None
    """
    pyautogui.press("super")
    time.sleep(0.1)
    pyautogui.typewrite(app_name)
    time.sleep(0.1)
    pyautogui.press("enter")

def screenshot(**args) -> None:
    """
    Takes sreenshot of the current screen.

    Parameters:
        None
    Returns:
        None
    """


    img = pyautogui.screenshot()
    img.save(DESKTOP_PATH)

def music():
    pass