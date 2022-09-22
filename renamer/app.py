import sys
from PyQt5 import QApplication as qapp
from .views import Window


def main():
    app = qapp(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
