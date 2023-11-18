import os
import time
# Replace this with the path to your directory
from DeleteGoogleChromeCache import your_directory


def is_chrome_running():
    try:
        # Command for Windows to check if Chrome is running
        output = os.popen('tasklist | find "chrome.exe"').read()
        return 'chrome.exe' in output
    except Exception as e:
        print(f"Error checking Chrome: {e}")
        return False


if __name__ == "__main__":
    while True:
        if not is_chrome_running():
            print("Chrome closed. Running cleanup...")
            delete_chrome_history_and_cache()
            break
        time.sleep(60)  # Wait 60 seconds before checking again
