
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("tarayıcı (nasıl yaptım bilmiyom)")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join('fotolar', 'ma-icon-128.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("versyon 1.0"))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))

        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("navigasyon")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        back_btn = QAction(QIcon(os.path.join('fotolar', 'arrow-180.png')), "Back", self)
        back_btn.setStatusTip("önceki sayfalara")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(os.path.join('fotolar', 'arrow-000.png')), "Forward", self)
        next_btn.setStatusTip("sonraki sayfalara")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(os.path.join('fotolar', 'arrow-circle-315.png')), "Reload", self)
        reload_btn.setStatusTip("yeniden yükle")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction(QIcon(os.path.join('fotolar', 'home.png')), "Home", self)
        home_btn.setStatusTip("ev")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.httpsicon = QLabel()  # Yes, really!
        self.httpsicon.setPixmap(QPixmap(os.path.join('fotolar', 'lock-nossl.png')))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_btn = QAction(QIcon(os.path.join('fotolar', 'cross-circle.png')), "Stop", self)
        stop_btn.setStatusTip("durdur")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("&File")

        open_file_action = QAction(QIcon(os.path.join('fotolar', 'disk--arrow.png')), "dosya aç...", self)
        open_file_action.setStatusTip("dosyadan aç")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join('fotolar', 'disk--pencil.png')), "f.Kaydet...", self)
        save_file_action.setStatusTip("bu sayfayı dosya yap")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        print_action = QAction(QIcon(os.path.join('fotolar', 'printer.png')), "yazdır...", self)
        print_action.setStatusTip("sayfayı yazdır")
        print_action.triggered.connect(self.print_page)
        file_menu.addAction(print_action)

        help_menu = self.menuBar().addMenu("&yardım")

        about_action = QAction(QIcon(os.path.join('fotolar', 'question.png')), "tarayıcı hakkında", self)
        about_action.setStatusTip("bunun hakkında biraz daha ögren")  # Hungry!
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        

        self.show()

        self.setWindowIcon(QIcon(os.path.join('fotolar', 'ma-icon-64.png')))

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - bilalin tarayıcısı(nası yaptım bunu aq)" % title)

    def navigate_mozarella(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "dosya aç", "",
                                                  "dil olmayan yazılım dili (*.htm *.html);;"
                                                  "tüm dosyalar (*.*)")

        if filename:
            with open(filename, 'r') as f:
                html = f.read()

            self.browser.setHtml(html)
            self.urlbar.setText(filename)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "f.Kaydet", "",
                                                  "dil olmayan yazılım dili (*.htm *html);;"
                                                  "tüm dosyalar (*.*)")

        if filename:
            html = self.browser.page().toHtml()
            with open(filename, 'w') as f:
                f.write(html)

    def print_page(self):
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.connect(self.browser.print_)
        dlg.exec_()

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):  # Does not receive the Url
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def update_urlbar(self, q):

        if q.scheme() == 'https':
            # Secure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join('fotolar', 'lock-ssl.png')))

        else:
            # Insecure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join('fotolar', 'lock-nossl.png')))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


app = QApplication(sys.argv)
app.setApplicationName("bilalin tarayıcısı (ben bunu nasıl yaptım aq)")
app.setOrganizationName("bilal")
app.setOrganizationDomain("google.com")

window = MainWindow()

app.exec_()