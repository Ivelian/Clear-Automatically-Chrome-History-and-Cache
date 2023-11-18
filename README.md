# Clear-Automatically-Chrome-History-and-Cache
 Python code that deletes the cache and history of Google Chrome to optimize it and improve privacy while monitoring it and executing the code when it is not active.

## First Script: Chrome Running Checker

The first script checks whether Google Chrome is running and, if not, executes a function to clear the browser's history and cache.

### Imports and Function Definitions

- `import os`: Imports the `os` module for interacting with the operating system.
- `import time`: Imports the `time` module for handling time-related operations.
- `from EliminarCacheGoogleChrome import eliminar_historial_y_cache_chrome`: Imports the `eliminar_historial_y_cache_chrome` function from another Python file.

### Function `is_chrome_running()`

- Checks if Google Chrome is running using a specific Windows command (`tasklist | find "chrome.exe"`).
- Returns `True` if Chrome is running, `False` otherwise. Captures and prints any errors that occur.

### Main Block (`if __name__ == "__main__"`)

- Executes an infinite loop (`while True`).
- Within the loop, checks if Chrome is not running (`if not is_chrome_running()`).
- If Chrome is not running, prints a message, calls `eliminar_historial_y_cache_chrome()`, and then breaks the loop (`break`).
- If Chrome is running, the program waits 5 seconds before checking again.

## Second Script: Chrome History and Cache Cleaner

The second script defines the `eliminar_historial_y_cache_chrome()` function, which is used to delete the history and cache of all user profile instances of Google Chrome.

### Imports

- `import sqlite3`: Imports the module for interacting with SQLite databases.
- `import os, glob, shutil`: Import modules for handling files and directories.

### Function `eliminar_historial_y_cache_chrome()`

- Finds the directory where Chrome stores user data.
- Uses `glob.glob` to get a list of all user profiles.
- Iterates through each profile:
  - Locates the history (`History`) and cache (`Cache`) files.
  - Deletes the URL history from the SQLite database in `History`.
  - Deletes the `History` and `History-journal` files if they exist.
  - Deletes the cache directory and then recreates it.
- Prints messages to inform about the actions performed or errors encountered.

## Integration of Both Scripts

- The first script acts as a monitor, waiting for Chrome to not be in execution to perform the cleaning.
- The second script is the one that effectively carries out the cleaning of the history and cache.
- These codes can be in separate files and are integrated by importing the `eliminar_historial_y_cache_chrome` function in the first file.

## Usage Context

These scripts would be useful in situations where there is a need to automate the cleaning of Chrome's history and cache, for example, in corporate environments to ensure data privacy and security, or on shared machines where a certain level of privacy is desired.

# Windows Task Scheduler Automation Guide

If you want to automate it, use the Windows Task Scheduler. In my case, I have configured it with 3 triggers on 2 different executables, which you can modify to your liking.

## First Executable
- **First run**: 8:30 AM
- **Repeats**: Every 1 hour over a period of 12 hours

## Second Executable
- **Trigger**: Every time the computer is locked

## Third Executable
- **Trigger**: When you are inactive for 1 minute
