import sys
from PyQt5.QtWidgets import QApplication
from src.rattrap import RattrapWindow

# TODO: Add functionality to save/load profiles

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = RattrapWindow()
    sys.exit(app.exec_())
