import sqlite3
import os
import glob
import shutil


def DeleteGoogleChromeCache():
    path_to_chrome = os.path.expanduser(
        '~\\AppData\\Local\\Google\\Chrome\\User Data')

    profile_paths = glob.glob(os.path.join(path_to_chrome, '*/'))
    deleted_history = False
    deleted_cache = False

    for profile_path in profile_paths:
        # Add for debugging
        print(f"Processing profile at: {profile_path}")
        history_path = os.path.join(profile_path, 'History')
        history_journal_path = os.path.join(profile_path, 'History-journal')
        cache_path = os.path.join(profile_path, 'Cache')

        # Delete history
        if os.path.exists(history_path):
            try:
                connection = sqlite3.connect(history_path)
                cursor = connection.cursor()
                cursor.execute("DELETE FROM urls")
                connection.commit()
                connection.close()
                deleted_history = True
                print(
                    f"The history of profile {profile_path} has been deleted.")
            except sqlite3.OperationalError as e:
                print(
                    f"Could not delete history from {profile_path}: {e}")

            if os.path.exists(history_journal_path):
                try:
                    os.remove(history_journal_path)
                    print(
                        f"The History-journal file in {profile_path} has been deleted.")
                except Exception as e:
                    print(
                        f"Could not delete History-journal file in {profile_path}: {e}")

        # Delete cache
        if os.path.exists(cache_path):
            try:
                shutil.rmtree(cache_path)
                deleted_cache = True
                print(f"The cache of profile {profile_path} has been deleted.")
            except Exception as e:
                print(f"Could not delete cache of {profile_path}: {e}")

        # Create cache directory if it doesn't exist
        if not os.path.exists(cache_path):
            os.makedirs(cache_path)

        if not os.path.exists(history_path):
            print(
                f"History database not found in {profile_path}")

    if not deleted_history:
        print("No history was deleted. Make sure Chrome is closed.")
    if not deleted_cache:
        print("No cache was deleted. Make sure Chrome is closed.")


if __name__ == "__main__":
    DeleteGoogleChromeCache()
