# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMenu
from PySide6.QtCore import QUrl
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget = QWidget()
        self.resize(800, 600)
        self.setWindowTitle("BrowseQt")
        self.hl = QHBoxLayout()
        self.bb = QPushButton(text="<")
        self.fb = QPushButton(text=">")
        self.rb = QPushButton(text="Reload")
        self.gobutton = QPushButton(text="Go")
        self.textedit = QLineEdit()
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
        self.webview.titleChanged.connect(lambda:self.setWindowTitle("BrowseQt - " + self.webview.title()))
        self.webview.iconChanged.connect(lambda: self.setWindowIcon(self.webview.icon()))
        def nt(x):
            self.webview.load(QUrl(x))
            self.setWindowTitle("BrowseQt - " + x)
            self.setWindowIcon(QIcon())
        def navigate():
            x = self.textedit.text()
            nt(x)
            self.hist.append(x)
            self.hi += 1
        self.gobutton.clicked.connect(navigate)
        self.fb.clicked.connect(self.webview.forward)
        self.bb.clicked.connect(self.webview.back)
        self.rb.clicked.connect(self.webview.reload)
        self.webview.urlChanged.connect(lambda: self.textedit.setText(self.webview.url().toString()))
        self.webview.load(QUrl("http://duckduckgo.com/"))
        self.textedit.setText("http://duckduckgo.com/")
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
