import sys
from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow
import qdarktheme
from net.client import Client


def main():
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()
    window = MainWindow()
    window.show()
    client = Client()
    client.sendMessage("zddxdxd")
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
