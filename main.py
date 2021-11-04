from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from functools import partial
from icodrops import icodrops
from icomarks import icomarks
from coincodex import coincodex
from cryptorank import cryptorank
from tradingview import tradingview
from bravenewcoin import bravenewcoin
from tradingeconomics import tradingeconomics
from worldbank import worldbank
from coinmarketcap import coinmarketcap
from airdrops import airdrops
from cryptoticker import cryptoticker
from airdropalert import airdropalert
# from analytics import  AnalyticsWidget

import os
import sys
import time
from multiprocessing import Process

# ============= Const variables define part =============

FROM_RESET, _ = loadUiType(os.path.join(
    os.path.dirname(__file__), "./UI/reset.ui"))

# ============= Worker Class for Worker Thread ============


class Worker(QObject):
    finished = pyqtSignal()
    scrap_id = 0

    def run(self):
        if(self.scrap_id == 1):
            icodrops()
        elif(self.scrap_id == 2):
            icomarks()
        elif(self.scrap_id == 3):
            coincodex()
        elif(self.scrap_id == 4):
            cryptorank()
        elif(self.scrap_id == 5):
            tradingview()
        elif(self.scrap_id == 6):
            bravenewcoin()
        elif(self.scrap_id == 7):
            tradingeconomics()
        elif(self.scrap_id == 8):
            worldbank()
        elif(self.scrap_id == 9):
            airdrops()
        elif(self.scrap_id == 10):
            coinmarketcap()
        elif(self.scrap_id == 11):
            cryptoticker()
        elif(self.scrap_id == 12):
            airdropalert()

        self.finished.emit()

# ============= Const variables define part =============


class MainWindow(QMainWindow, FROM_RESET):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.setupUi(self)

        px = QPixmap("./images/back.png")
        px = px.scaled(self.back.size(), Qt.IgnoreAspectRatio)
        self.back.setPixmap(px)

        self.setWindowIcon(QIcon('./images/icon.png'))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.iconLabel.setPixmap(QPixmap("./images/icon.png"))
        self.btnMinimize.setIcon(
            QIcon(QPixmap("./images/icon_window_minimize.png")))
        self.btnClose.setIcon(QIcon(QPixmap("./images/icon_window_close.png")))

        self.btnClose.clicked.connect(self.close)
        self.btnMinimize.clicked.connect(self.showMinimized)
        self.attach_btn1.clicked.connect(self.scrape_icodrops)
        self.attach_btn2.clicked.connect(self.scrape_icomarks)
        self.attach_btn3.clicked.connect(self.scrape_coincodex)
        self.attach_btn4.clicked.connect(self.scrape_cryptorank)
        self.attach_btn5.clicked.connect(self.scrape_tradingview)
        self.attach_btn6.clicked.connect(self.scrape_bravenewcoin)
        self.attach_btn7.clicked.connect(self.scrape_tradingeconomics)
        self.attach_btn8.clicked.connect(self.scrape_worldbank)
        self.attach_btn9.clicked.connect(self.scrape_airdrops)
        self.attach_btn10.clicked.connect(self.scrape_coinmarketcap)
        self.attach_btn11.clicked.connect(self.scrape_cryptoticker)
        self.attach_btn12.clicked.connect(self.scrape_airdropalert)

    def scrape_cryptoticker(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 11
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn11.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn11.setText("Extract"))
        )

    def scrape_airdropalert(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 12
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn12.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn12.setText("Extract"))
        )

    def scrape_coinmarketcap(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 10
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn10.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn10.setText("Extract"))
        )

    def scrape_airdrops(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 9
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn9.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn9.setText("Extract"))
        )

    def scrape_worldbank(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 8
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn8.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn8.setText("Extract"))
        )

    def scrape_tradingeconomics(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 7
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn7.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn7.setText("Extract"))
        )

    def scrape_bravenewcoin(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 6
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn6.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn6.setText("Extract"))
        )

    def scrape_tradingview(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 5
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn5.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn5.setText("Extract"))
        )

    def scrape_cryptorank(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 4
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn4.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn4.setText("Extract"))
        )

    def scrape_icodrops(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 1
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn1.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn1.setText("Extract"))
        )

    def scrape_icomarks(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 2
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn2.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn2.setText("Extract"))
        )

    def scrape_coincodex(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 3
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn3.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn3.setText("Extract"))
        )

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Application Close', 'Are you sure you want to close the application?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            self.close()
        else:
            event.ignore()

# ============= Application Start Point =============


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    try:
        main()
    except Exception as why:
        print(why)
