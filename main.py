# FILE: main.py

import sys
import json
import os
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

def get_base_path():
    """
    Get the base path for the application, which is the directory of the
    executable in a PyInstaller bundle, or the directory of the script otherwise.
    """
    if getattr(sys, 'frozen', False):
        # We are running in a bundle (e.g., a PyInstaller exe)
        # sys.executable is the path to the exe
        return os.path.dirname(sys.executable)
    else:
        # We are running in a normal Python environment
        # __file__ is the path to the script
        return os.path.dirname(os.path.abspath(__file__))

# Define the config file path relative to the application's base path
BASE_PATH = get_base_path()
CONFIG_FILE = os.path.join(BASE_PATH, "config.json")


def load_or_create_config():
    """
    Loads configuration from config.json located next to the executable.
    If the file doesn't exist, it creates a default one there.
    """
    if not os.path.exists(CONFIG_FILE):
        print(f"'{CONFIG_FILE}' not found. Creating a default one.")
        default_config = {
            "number_of_windows": 2,
            "url": "https://k12.instructure.com/courses/2159019"
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(default_config, f, indent=4)
        return default_config
    else:
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Error: '{CONFIG_FILE}' is not a valid JSON file. Using default settings.")
            return {"number_of_windows": 2, "url": "https://qt.io"} # Fallback

def main():
    """
    The main entry point for the application.
    """
    config = load_or_create_config()

    app = QApplication(sys.argv)
    
    window = MainWindow(config)
    window.showMaximized()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()