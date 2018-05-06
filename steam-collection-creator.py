
import sys
import json

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QDesktopWidget, QLineEdit, QLabel, QPushButton, \
    QGridLayout, QDialog, QVBoxLayout, QTextEdit, QAction, QComboBox
from collections import OrderedDict


def generate_button(info, active):
    if active:
        button = "[img]" + info["active_button_link"] + "[/img]"
    else:
        button = "[url=" + info["workshop_link"] + "][img]" + info["normal_button_link"] + "[/img][/url]"
    return button


def generate_description(data, selected_name):
    description = ""
    for item_name, item_info in data.items():
        description += generate_button(item_info, selected_name == item_name)
    return description


class MainWindow(QMainWindow):

    def __init__(self, data, parent=None):
        super(MainWindow, self).__init__(parent)
        self.center()
        self.main_widget = MainWidgets(data)
        self.setCentralWidget(self.main_widget)
        self.setWindowTitle('Steam Collection Creator')
        self.create_menu_bar()

    def create_menu_bar(self):
        """
        Create the app menu bar
        :return:
        """
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")
        help_menu = main_menu.addMenu("Help")

        exit_button = QAction('Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit the app')
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)

        about_button = QAction('About', self)
        about_button.setShortcut('Ctrl+H')
        about_button.setStatusTip('Get help')
        about_button.triggered.connect(self.display_help_dialog)
        help_menu.addAction(about_button)

    def display_help_dialog(self):
        """
        Display the help dialog showing info about the app
        :return:
        """
        dialog = HelpDialog(self)
        dialog.exec_()
        dialog.deleteLater()

    def center(self):
        """
        Center the app window in the screen
        :return:
        """
        rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())


class MainWidgets(QWidget):

    def __init__(self, data):
        self.main_layout = QGridLayout()
        super().__init__()
        self.data = data
        self.item_name_label = QLabel("Item Name")
        self.item_name_edit = QComboBox()
        self.generate_button = QPushButton("Generate !")
        self.generated_code_label = QLabel("Select an item and Hit 'Generate!'")
        self.generated_code_edit = QLineEdit()
        self.init_ui()

    def init_ui(self):
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.item_name_label, 0, 0, 1, 1)
        self.item_name_edit.addItem("")
        self.item_name_edit.addItems(self.data.keys())
        self.main_layout.addWidget(self.item_name_edit, 0, 1, 1, 18)
        self.generate_button.setToolTip("Generate and copy code to clipboard")
        self.generate_button.clicked.connect(self.start_generating)
        self.main_layout.addWidget(self.generate_button, 0, 19, 1, 1)
        self.main_layout.addWidget(self.generated_code_label, 1, 0, 1, 20)
        self.main_layout.addWidget(self.generated_code_edit, 2, 0, 1, 20)

    def start_generating(self):

            name = self.item_name_edit.currentText()
            generated_code = generate_description(data, name)
            if name == "":
                self.generated_code_label.setText("Generated code without active item:")
            else:
                self.generated_code_label.setText("Generated description with item '" + name + "' active:")
            self.generated_code_edit.setText(generated_code)
            QApplication.clipboard().setText(generated_code)


class HelpDialog(QDialog):
    """
    help window showing information about thee app
    """
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.setWindowTitle('Steam Collection Creator - About')
        title = QLabel("Steam Collection Creator")
        font = title.font()
        font.bold()
        font.setPixelSize(20)
        title.setFont(font)
        title.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(title)
        info = QLabel("This app lets you generate the necessary code to display a collection of items in your "
                      "workshop description\nMake sure to complete the 'data.json' file with all the necessay "
                      "information\nTo use the app, simply select the name of the active item (the one you are "
                      "generating the code for) and hit 'Generate!'\nThen, simply copy-paste the generated code into "
                      "your description!\nIf no name is given, it generates the code with no active item\n\nMade by "
                      "Keplyx, Licensed under GPLv3, available on GitHub")
        link = QLabel("<a href='https://github.com/Keplyx/steam-collection-creator'>https://github.com/Keplyx/steam"
                      "-collection-creator</a>")
        self.main_layout.addWidget(info)
        link.linkActivated.connect(self.open_link)
        link.openExternalLinks()
        self.main_layout.addWidget(link)

    def open_link(self, url):
        QDesktopServices.openUrl(QUrl(url))

if __name__ == '__main__':
    with(open("data.json")) as f:
        data = json.load(f, object_pairs_hook=OrderedDict)  # preserve order
        app = QApplication(sys.argv)
        main_window = MainWindow(data)
        main_window.show()
        sys.exit(app.exec_())

