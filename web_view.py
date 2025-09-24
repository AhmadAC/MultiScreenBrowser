from PySide6.QtCore import Qt
from PySide6.QtWebEngineWidgets import QWebEngineView

class WebView(QWebEngineView):
    """
    A custom QWebEngineView widget configured for touch interaction.
    
    This class encapsulates the browser view and enables the necessary
    attributes for multi-touch gestures like pinch-to-zoom within the 
    web content. By setting the WA_AcceptTouchEvents attribute, the widget
    is configured to receive and process raw touch events from the system.
    """
    def __init__(self, parent=None):
        """
        Initializes the WebView instance.
        
        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        
        # This is the crucial line that enables the widget to receive touch events.
        # Without this, all touch interactions would be translated into mouse events,
        # preventing multi-touch gestures from working correctly.
        self.setAttribute(Qt.WA_AcceptTouchEvents, True)