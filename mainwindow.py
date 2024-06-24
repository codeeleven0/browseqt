# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QStyle
from PySide6.QtCore import QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtWebEngineWidgets import QWebEngineView
import ctypes
myappid = 'codex.tav.browseqt.v1'
try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except:
    pass
try:
    import pyi_splash
    pyi_splash.update_text("Loading...")
except:
    pass
class HelpDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.raise_()
        self.activateWindow()
        self.setWindowTitle("About CodeX BrowseQt")
        self.resize(300, 100)
        self.qtlogo = self.style().standardIcon(getattr(QStyle, "SP_TitleBarMenuButton"))
        self.oklogo = self.style().standardIcon(getattr(QStyle, "SP_DialogOkButton"))
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.logo = QLabel(text="", pixmap=QPixmap("BrowseQt.png"))
        self.aboutlabel = QLabel(text="CodeX BrowseQt™ - Copyright © 2024 CodeX Software and Cybersecurity\nPowered by Qt")
        self.hlay = QHBoxLayout()
        self.qtabout = QPushButton(icon=self.qtlogo, text="About Qt")
        self.qtabout.clicked.connect(app.aboutQt)
        self.exit = QPushButton(icon=self.oklogo, text="Close")
        self.exit.clicked.connect(self.close)
        self.hlay.addWidget(self.qtabout)
        self.hlay.addWidget(self.exit)
        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.aboutlabel)
        self.layout.addLayout(self.hlay)
        self.widget.setLayout(self.layout)
        self.setWindowIcon(self.qtlogo)
        self.setCentralWidget(self.widget)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.raise_()
        self.activateWindow()
        self.qtlogo = self.style().standardIcon(getattr(QStyle, "SP_TitleBarMenuButton"))
        self.backarrow = self.style().standardIcon(getattr(QStyle, "SP_ArrowBack"))
        self.forwarrow = self.style().standardIcon(getattr(QStyle, "SP_ArrowForward"))
        self.commlink = self.style().standardIcon(getattr(QStyle, "SP_CommandLink"))
        self.reload = self.style().standardIcon(getattr(QStyle, "SP_BrowserReload"))
        self.info = self.style().standardIcon(getattr(QStyle, "SP_FileDialogInfoView"))
        self.widget = QWidget()
        self.resize(1000, 1000)
        self.setWindowIcon(self.qtlogo)
        self.setWindowTitle("CodeX BrowseQt")
        self.hl = QHBoxLayout()
        self.bb = QPushButton(text="", icon=self.backarrow)
        self.fb = QPushButton(text="", icon=self.forwarrow)
        self.rb = QPushButton(text="", icon=self.reload)
        self.gobutton = QPushButton(text="", icon=self.commlink)
        self.helpbutton = QPushButton(text="", icon=self.info)
        self.dialog = HelpDialog()
        self.helpbutton.clicked.connect(self.dialog.show)
        self.textedit = QLineEdit()
        self.hl.addWidget(self.helpbutton)
        self.hl.addWidget(self.rb)
        self.hl.addWidget(self.bb)
        self.hl.addWidget(self.fb)
        self.hl.addWidget(self.textedit)
        self.hl.addWidget(self.gobutton)
        self.vl = QVBoxLayout()
        self.webview = QWebEngineView()
        self.vl.addLayout(self.hl)
        self.vl.addWidget(self.webview)
        self.widget.setLayout(self.vl)
        self.setCentralWidget(self.widget)
        self.webview.titleChanged.connect(lambda:self.setWindowTitle("CodeX BrowseQt - " + self.webview.title()))
        def cwbi():
            self.setWindowIcon(self.qtlogo)
            i = self.webview.icon()
            self.setWindowIcon(i)
        self.webview.iconChanged.connect(cwbi)
        def nt(x):
            self.webview.load(QUrl(x))
            self.setWindowTitle("BrowseQt - " + x)
            self.setWindowIcon(self.qtlogo)
        def navigate():
            x = self.textedit.text()
            nt(x)
        self.textedit.returnPressed.connect(navigate)
        self.gobutton.clicked.connect(navigate)
        self.fb.clicked.connect(self.webview.forward)
        self.bb.clicked.connect(self.webview.back)
        self.rb.clicked.connect(self.webview.reload)
        def updua():
            x = lambda: self.textedit.setText(self.webview.url().toString())
            x()

        self.webview.urlChanged.connect(updua)
        self.webview.load(QUrl("https://start.duckduckgo.com/"))
        self.textedit.setText("https://start.duckduckgo.com/")
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    try:
        import pyi_splash
        pyi_splash.update_text("Done!")
    except:
        pass
    try:
        import pyi_splash
        pyi_splash.close()
    except:
        pass
    
    window.show()
    sys.exit(app.exec())
