import sys, os
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import Qt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
pwd=b"i7uJ7ZDx3O5BAHZWiCV4c4XrES0Jotgm"
msg=b"Hello World, My name is Fernando!!!! The password is 256 bit long."
aed=b"saltallovermypassword"
iv=os.urandom(27)
cipher=Cipher(algorithms.AES(pwd), modes.GCM(iv), backend=backend)
e=cipher.encryptor()
e.authenticate_additional_data(aed)
ct=e.update(msg) + e.finalize()
tag=e.tag
cipher=Cipher(algorithms.AES(pwd), modes.GCM(iv,tag), backend=backend)
d=cipher.decryptor()
d.authenticate_additional_data(aed)
clear=d.update(ct)+d.finalize()
assert clear,msg
x = clear.decode()

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("CryptX Chat")
        label = QLabel(x)
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

if __name__=="__main__":
     app = QApplication(sys.argv)
     win = VentanaPrincipal()
     win.show()
     sys.exit(app.exec_())