# FILE: main_window.py

from PySide6.QtWidgets import QMainWindow
from central_widget import CentralWidget

class MainWindow(QMainWindow):
    """
    The main application window. It accepts a configuration dictionary
    and passes it to its CentralWidget.
    """
    def __init__(self, config):
        """
        Initializes the MainWindow instance.
        
        Args:
            config (dict): A dictionary containing application settings.
        """
        super().__init__()

        self.setWindowTitle("Modular Multi-Touch Dual-Website Browser")

        # Create an instance of our custom CentralWidget, passing the config.
        central_widget = CentralWidget(config, self)

        self.setCentralWidget(central_widget)