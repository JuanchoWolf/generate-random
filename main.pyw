from src.ui_base import *
from src.logistic import *

if __name__ == '__main__':
    app = QApplication()
    root = QWidget()
    ui = Ui_applicationUi()
    ui.setupUi(root)
    root.show()

    exit(app.exec())