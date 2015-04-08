import sys
from PyQt4 import QtCore, QtGui

from gsmui import Ui_GSMConfigurationUtility

import threading

import serial

connected = False

ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 9600
ser.timeout = None
ser.xonxoff = False
ser.rtscts = False
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE


class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_GSMConfigurationUtility()
        self.ui.setupUi(self)

        self.ui.B_Open.setEnabled(True)
        self.ui.B_DisableAutoBaud.setEnabled(False)
        self.ui.B_MsgFormat.setEnabled(False)
        self.ui.B_Call.setEnabled(False)
        self.ui.B_halt.setEnabled(False)

        self.ui.B_Open.clicked.connect(self.openCom)
        self.ui.B_DisableAutoBaud.clicked.connect(self.disableAutoBaud)
        self.ui.B_MsgFormat.clicked.connect(self.changeMsgFormat)
        self.ui.B_Call.clicked.connect(self.makeCall)
        self.ui.B_halt.clicked.connect(self.haltCall)


    def openCom(self):
        # print 'opening comport'
        self.ui.textLog.append('Opening Comport\n')
        try:
            portName = str(self.ui.ComPort.text())
            if (len(portName)>3):
                ser.port = portName
            else:
                self.ui.textLog.append('Defaulting to ttyUSB0\n')
            ser.open()
            ser.flushInput()
            ser.flushOutput()

            global connected
            connected = True
            thread = threading.Thread(target=self.read_from_port, args=(ser,))
            thread.start()

            self.ui.B_Open.setDisabled(True)
            self.ui.B_DisableAutoBaud.setEnabled(True)
            self.ui.B_MsgFormat.setEnabled(True)
            self.ui.B_Call.setEnabled(True)
            self.ui.B_halt.setEnabled(True)
            self.ui.textLog.append('Com port opened successfully\n')



        except:
             self.ui.textLog.append ('Cannot open serial port\n')


    def disableAutoBaud(self):
        # print 'disable auto baudrate'
        ser.write('AT+IPR=9600;&W\r\n')
        self.ui.textLog.append('Auto bauding disabled\n')

    def changeMsgFormat(self):
        # print 'change Msg Format'
        ser.write('AT+CMGF=1;&W\r\n')
        self.ui.textLog.append('Text mode enabled\n')

    def makeCall(self):
        # print 'make Call'
        phNum = str(self.ui.PhNumber.text())
        if ((len(phNum) == 10) or (len(phNum) == 10)):
            ser.write('ATD'+ phNum + ';\r\n')
            self.ui.textLog.append('Call in progress\n')
        else:
            self.ui.textLog.append('Check phone number\n')

    def haltCall(self):
        # print 'Halt call'
        ser.write('ATH\r\n')
        self.ui.textLog.append('Call disconnected\n')


    def read_from_port(self,ser):
        global connected
        while True & connected:
            #print("test")
            reading = ser.readline()
            if len(reading) > 0:
                reading = str(reading).rstrip()
                if len(reading) > 0:
                    try:
                        reading.decode('ascii')
                        self.ui.textLog.insertPlainText(QtCore.QString(reading+'\n'))
                        # self.SerialLog.insertPlainText(QtCore.QString(reading+'\n'))
                    except:
                        self.ui.textLog.insertPlainText(QtCore.QString('Non ascii characters'+'\n'))
                        # self.SerialLog.insertPlainText(QtCore.QString('Non ascii characters'+'\n'))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
    # thread.stop()
