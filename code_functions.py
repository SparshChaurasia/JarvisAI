import os
import webbrowser
from datetime import datetime
import time
import pyautogui

DESKTOP_PATH = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

# OS Functions
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


def shutdown() -> None:
    """
    Shuts down the computer.

    Parameters:
        None
    Returns:
        None
    """
    os.system('shutdown -s')

def screenshot(**args) -> None:
    """
    Takes sreenshot of the current screen and saves it to desktop.

    Parameters:
        None
    Returns:
        None
    """
    n = 1
    for f in os.listdir(DESKTOP_PATH):
        if "screenshot" in f:
            n += 1
    pyautogui.screenshot(f"{DESKTOP_PATH}\screenshot{n}.png")

# Open Apps and Websites
def open_apps(app_name: str) -> None:
    """
    Opens the given apps.

    Parameters:
        string: app_name
    Returns:
        None
    """

    print("app name:", app_name)
    pyautogui.press("super")
    time.sleep(0.1)
    pyautogui.typewrite(app_name)
    time.sleep(0.4)
    pyautogui.press("enter")

def open_websites(website_url: str) -> None:
    """
    Opens the given website.

    Parameters:
        string: website_url
    Returns:
        None
    """
    print("url:", website_url)
    webbrowser.open(url=website_url, autoraise=True)
