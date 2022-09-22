# Provides the main window

import sys
from PyQt5 import QtWidgets
from .ui.window import Ui_Window
sys.path.insert(0, 'C:\\Users\\Rhine\\Documents\\GitHub\\Bulk-File-Rename\\ui')


class Window(QtWidgets, Ui_Window):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def _setupUI(self):
        self._setupUI(self)
