# FILE: central_widget.py

from PySide6.QtWidgets import QWidget, QHBoxLayout, QFrame
from PySide6.QtCore import QUrl
from web_view import WebView

class CentralWidget(QWidget):
    """
    The central widget that dynamically creates a specified number of web views
    based on a configuration file.
    """
    def __init__(self, config, parent=None):
        """
        Initializes the CentralWidget instance.
        
        Args:
            config (dict): Configuration dictionary with 'number_of_windows' and 'url'.
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        
        # Get settings from the config, providing safe defaults.
        num_windows = config.get("number_of_windows", 2)
        url_to_load_str = config.get("url", "https://qt.io") # Default URL if missing

        # Clamp the number of windows between 1 and 4 for practical use.
        num_windows = max(1, min(num_windows, 4))
        
        url_to_load = QUrl(url_to_load_str)

        # Create a list to hold all our web view instances
        self.web_views = []
        for _ in range(num_windows):
            view = WebView()
            view.setUrl(url_to_load)
            self.web_views.append(view)

        self._setup_layout()

    def _setup_layout(self):
        """
        Creates and configures the layout dynamically based on the number of web views.
        """
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Loop through the web views and add them to the layout with separators
        for i, web_view in enumerate(self.web_views):
            # Add the web view with a stretch factor of 1 so they all share space equally
            layout.addWidget(web_view, 1)

            # Add a separator AFTER each view, except for the very last one
            if i < len(self.web_views) - 1:
                separator = QFrame()
                separator.setFrameShape(QFrame.Shape.VLine)
                separator.setFrameShadow(QFrame.Shadow.Sunken)
                separator.setFixedWidth(20)
                separator.setStyleSheet("background-color: black;")
                layout.addWidget(separator)