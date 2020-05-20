from PySide2.QtWidgets import *

class LabeledTextField(QWidget):
    def __init__(self, text):
        QWidget.__init__(self)
        self.__text = text
        self.layout = QHBoxLayout()


        self.label = QLabel(self.__text)
        self.layout.addWidget(self.label)

        self.notifPanel = QTextEdit()
        self.layout.addWidget(self.notifPanel)

        self.notifPanel.setMaximumHeight(30)

        self.setLayout(self.layout)


class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.layout = QVBoxLayout()


        self.label1 = LabeledTextField("IP address")
        self.layout.addWidget(self.label1)

        self.label2 = LabeledTextField("User")
        self.layout.addWidget(self.label2)

        self.label3 = LabeledTextField("Password")
        self.layout.addWidget(self.label3)

        self.setLayout(self.layout)




if __name__ == "__main__":
   app = QApplication([])
   ihm = ConfigurationDialog()
   ihm.show()
   app.exec_()

