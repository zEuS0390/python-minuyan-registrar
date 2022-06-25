from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QTabWidget, QTableWidget
)

try:
    import rc.resources
    from src.constants import *
    from src.jhs.view import View
except:
    import os, sys
    sys.path.insert(0, os.path.dirname(sys.path[0]))
    from configparser import ConfigParser
    from constants import *
    import jhs.view, shs.view
    import rc.resources

class AllForms(QWidget):

    def __init__(self, parser, parent=None):
        super(AllForms, self).__init__(parent)
        self.parser = parser
        self.parser.read(os.path.join(CONFIG_DIR, APP_CONFIG))
        self.setup_UI()

    def setup_UI(self):
        self.setMinimumSize(self.parser.getint("application", "min_width"), 
                            self.parser.getint("application", "min_height"))
        self.setWindowTitle(self.parser.get("application", "window_title"))
        self.mainlayout = QVBoxLayout()
        self.formslayout = QHBoxLayout()
        self.setup_tabs()
        self.setLayout(self.mainlayout)

    def setup_tabs(self):
        self.tabwidget = QTabWidget()
        self.mainlayout.addWidget(self.tabwidget)
        self.jhs_view = jhs.view.View()
        self.shs_view = shs.view.View()
        self.tabwidget.addTab(self.jhs_view, "JHS Form")
        self.tabwidget.addTab(self.shs_view, "SHS Form")

    def setup_allforms_table(self):
        self.allformstable = QTableWidget()
        self.formslayout.addWidget(self.allformstable)

if __name__=="__main__":
    parser = ConfigParser()
    app = QApplication(sys.argv)
    widget = AllForms(parser)
    widget.show()
    sys.exit(app.exec())