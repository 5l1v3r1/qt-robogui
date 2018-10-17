from PyQt4  import QtCore, QtGui
from networktables import NetworkTables 

ip = "10.71.8.2"

NetworkTables.initialize(server = ip)
sd = NetworkTables.getTable("datatable")

class LEDControlPanel(QtGui.QWidget):
	"""docstring for LEDControlPanel."""
	def __init__(self, settings={}):
		
		super(LEDControlPanel, self).__init__()
		self.settings = settings
		
		self.v_layout = QtGui.QVBoxLayout()
		self.v_layout.setAlignment(QtCore.Qt.AlignTop)
		
		labelLED = QtGui.QLabel("LED Control Panel")
		buttonSetLEDToRed =  QtGui.QPushButton("Red")
		buttonSetLEDToMagenta = QtGui.QPushButton("Magenta")
		buttonSetLEDToBlue = QtGui.QPushButton("Blue")
		
		buttonSetLEDToRed.clicked.connect(self.on_redButton_click)
		buttonSetLEDToMagenta.clicked.connect(self.on_magentaButton_click)
		buttonSetLEDToBlue.clicked.connect(self.on_blueButton_click)
		
		self.v_layout.addWidget(labelLED)
		self.v_layout.addWidget(buttonSetLEDToRed)
		self.v_layout.addWidget(buttonSetLEDToBlue)
		self.v_layout.addWidget(buttonSetLEDToMagenta)
		self.setLayout(self.v_layout)

	def on_redButton_click(self):
		print ("LEDs have been changed to red succesfully")
		sd.putNumber("LEDColor", 1)
	def on_blueButton_click(self):
		print ("LEDs have been changed to blue succesfully")
		sd.putNumber("LEDColor", 2)
	def on_magentaButton_click(self):
		print ("LEDs have been changed to magenta succesfully")
		sd.putNumber("LEDColor", 0)
		
class BottomStatusPanel(QtGui.QWidget):
    """docstring for BottomStatusPanel."""
    def __init__(self, settings={}):
        super(BottomStatusPanel, self).__init__()
        self.settings = settings

        self.h_layout = QtGui.QHBoxLayout()
        self.h_layout.setAlignment(QtCore.Qt.AlignLeft)

        self.h_layout.addWidget(QtGui.QLabel("Last Played Track:	" + sd.getString("lastPlayed", "")))

        self.setLayout(self.h_layout)


class MainWidgetArea(QtGui.QWidget):
    """docstring for MainPanelArea."""
    def __init__(self, settings={}):
        super(MainWidgetArea, self).__init__()
        self.settings = settings
    
        self.h_layout = QtGui.QHBoxLayout()
        self.h_layout.setAlignment(QtCore.Qt.AlignLeft)	
		
        self.h_layout.addWidget(QtGui.QLabel("Robot Status: " + sd.getString("roboStat"))
        
        self.setLayout(self.x_layout)



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
