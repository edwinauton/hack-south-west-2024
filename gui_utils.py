import json
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QSizePolicy, QFrame, QDoubleSpinBox

from stock import Stock


# Function to create a button with the given text
def create_button(text):
    button = QPushButton()
    button.setText(str(text))
    return button


# Function to create a label with the given text
def create_label(text):
    label = QLabel(str(text))
    label.setAlignment(Qt.AlignCenter)
    label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
    return label


def create_spinbox():
    spinbox = QDoubleSpinBox()
    return spinbox


# Function to create a dividing horizontal line
def create_line():
    line = QFrame()
    line.setFrameShape(QFrame.HLine)
    line.setObjectName("line")
    return line


# Function to add a '$' sign in front of a value
def format(data):
    string = str(data)
    if string[0] == "-":
        return "-$" + string[1:]
    else:
        return "$" + string


# Function to colour regular loss/gain figures
def colour(label):
    if "-" in label.text():
        label.setStyleSheet("color: #e14141;")
    else:
        label.setStyleSheet("color: #029c29;")


# Function to create a list of stocks from a file
def get_stocks_list():
    # Read stocks stored in file
    with open("stock_record.json") as f:
        data = json.load(f)

    stocks_list = []

    # Read data from files provided by API
    for subdir, dirs, files in os.walk("api_data"):
        for file in files:
            filepath = subdir + os.sep + file
            if file.endswith(".json"):
                filename = os.path.splitext(file)[0]
                try:
                    number_of_stocks = data[filename]
                except KeyError:
                    number_of_stocks = 0
                stocks_list.append(Stock(filepath, number_of_stocks))

    return stocks_list
