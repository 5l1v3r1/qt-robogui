import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    def run(self):
        self.enabled = True
        cap = cv2.VideoCapture(0)
        while self.enabled:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.initUI()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))


    def initUI(self):
        self.setWindowTitle("ASD")
        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.resize(1800, 1200)
        # create a label
        self.label = QLabel(self)
        # self.label.move(280, 120)
        self.label.resize(640, 480)

        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
