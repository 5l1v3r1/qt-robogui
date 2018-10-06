from PyQt4 import QtCore, QtGui




class LEDControlPanel(QtGui.QWidget):
    """docstring for LEDControlPanel."""
    def __init__(self, settings={}):
        super(LEDControlPanel, self).__init__()
        self.settings = settings

        self.v_layout = QtGui.QVBoxLayout()
        self.v_layout.setAlignment(QtCore.Qt.AlignTop)


        for i in range(5):
            button = QtGui.QPushButton("merhaba" + str(i))
            button.clicked.connect(self.on_button_click)
            self.v_layout.addWidget(button)

        self.setLayout(self.v_layout)

    def on_button_click(self):
        print "CLICKED"



class BottomStatusPanel(QtGui.QWidget):
    """docstring for BottomStatusPanel."""
    def __init__(self, settings={}):
        super(BottomStatusPanel, self).__init__()
        self.settings = settings

        self.h_layout = QtGui.QHBoxLayout()
        self.h_layout.setAlignment(QtCore.Qt.AlignLeft)

        for i in range(3):
            self.h_layout.addWidget(QtGui.QLabel("Hello i am label " + str(i)))

        self.setLayout(self.h_layout)


class MainWidgetArea(QtGui.QWidget):
    """docstring for MainPanelArea."""
    def __init__(self, settings={}):
        super(MainWidgetArea, self).__init__()
        self.settings = settings

        self.h_layout = QtGui.QHBoxLayout()
        self.h_layout.setAlignment(QtCore.Qt.AlignLeft)

        for i in range(3):
            self.h_layout.addWidget(QtGui.QLabel("Hello i am label " + str(i)))

        self.setLayout(self.h_layout)



class VoltranMainWindow(QtGui.QMainWindow):
    """docstring for VoltranMainWindow."""
    def __init__(self, settings={}):
        super(VoltranMainWindow, self).__init__()
        self.settings = settings

        centralWidget = QtGui.QWidget()
        MainLayout = QtGui.QHBoxLayout()

        mainRightLayout = QtGui.QHBoxLayout()
        mainRightLayout.setAlignment(QtCore.Qt.AlignRight)

        mainLeftLayout = QtGui.QHBoxLayout()
        mainLeftLayout.setAlignment(QtCore.Qt.AlignLeft)


        controlPanel = LEDControlPanel()
        mainRightLayout.addWidget(controlPanel)


        leftVerticalLayout = QtGui.QVBoxLayout()

        # top hizala
        leftVerticalTopLayout = QtGui.QVBoxLayout()
        leftVerticalTopLayout.setAlignment(QtCore.Qt.AlignTop)
        leftVerticalLayout.addLayout(leftVerticalTopLayout)

        # RESIM OLUSTUR
        logo_label = QtGui.QLabel()
        image = QtGui.QPixmap("./Source/AppSource/Images/volTRan.png")
        # logo_label.setMask(image.mask())
        logo_label.setPixmap(image)
        logo_label.setFixedWidth(50)
        logo_label.setFixedHeight(50)
        # RESIM OLUSTUR

        leftVerticalTopLayout.addWidget(logo_label)

        # WIDGET LARI EKLE - KAMERA FALAN FILAN
        mainWidgetArea = MainWidgetArea()
        # leftVerticalTopLayout.addWidget(mainWidgetArea)
        leftVerticalLayout.addWidget(mainWidgetArea)


        # asagi hizala
        leftVerticalBottomLayout = QtGui.QVBoxLayout()
        leftVerticalBottomLayout.setAlignment(QtCore.Qt.AlignBottom)
        leftVerticalLayout.addLayout(leftVerticalBottomLayout)

        statusWidget = BottomStatusPanel()
        leftVerticalBottomLayout.addWidget(statusWidget)







        mainLeftLayout.addLayout(leftVerticalLayout)

        MainLayout.addLayout(mainLeftLayout)
        MainLayout.addLayout(mainRightLayout)
        centralWidget.setLayout(MainLayout)
        self.setCentralWidget(centralWidget)
