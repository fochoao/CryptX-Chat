import sys, os
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("CryptX Chat")
        label = QLabel("Hello World!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

if __name__=="__main__":
     app = QApplication(sys.argv)
     win = VentanaPrincipal()
     win.show()
     sys.exit(app.exec_())
