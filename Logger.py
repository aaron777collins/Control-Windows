# Make a logger using PyQT5 to display messages in a GUI
# Also save to a log file

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QVBoxLayout, QPushButton
import logging
import logging.handlers
import datetime

class Logger(QtWidgets.QWidget):

    # def __new__(cls, *args, **kwargs):
    #     return super(Logger, cls).__new__(cls, *args, **kwargs)

    def __init__(self, title="Logger"):
        super().__init__()
        self.title = title
        self.left = 10
        self.top = 10
        self.width = 660
        self.height = 500
        self.initUI()
        self.initLogger()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QPlainTextEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(600, 400)

        self.button = QPushButton('Close', self)
        self.button.move(20, 440)
        self.button.clicked.connect(self.close)

        self.show()

    def initLogger(self):
        # create logger
        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.DEBUG)

        # create file handler which logs even debug messages
        fh = logging.handlers.RotatingFileHandler('test.log', maxBytes=1000000, backupCount=5)
        fh.setLevel(logging.DEBUG)

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        self.logger.debug('This is a debug message')
        self.logger.info('This is an info message')
        self.logger.warning('This is a warning')
        self.logger.error('This is an error message')
        self.logger.critical('This is a critical error message')

        self.logger.debug('This is another debug message')

    def updateLog(self):
        with open('test.log', 'r') as f:
            data = f.read()
            self.textbox.setPlainText(data)

        self.textbox.moveCursor(self.textbox.textCursor().End)

    def closeEvent(self, event):
        self.updateLog()
        event.accept()


if __name__ == '__main__':
    app = QApplication([])
    window = Logger()
    window.show()
    app.exec()
