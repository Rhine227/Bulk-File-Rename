# -*- coding: utf-8 -*-
# renamer/views.py

"""This module provides the RP Renamer main window."""

from PyQt5.QtWidgets import QWidget
from ui.window import Ui_Window


class Window(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        self._setupUI()

    def _setupUI(self):
        self.setupUi(self)
