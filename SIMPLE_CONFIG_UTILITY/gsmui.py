# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gsmui.ui'
#
# Created: Fri Apr  3 10:00:04 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GSMConfigurationUtility(object):
    def setupUi(self, GSMConfigurationUtility):
        GSMConfigurationUtility.setObjectName(_fromUtf8("GSMConfigurationUtility"))
        GSMConfigurationUtility.resize(402, 305)
        self.horizontalLayoutWidget = QtGui.QWidget(GSMConfigurationUtility)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 381, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ComPort = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.ComPort.setObjectName(_fromUtf8("ComPort"))
        self.horizontalLayout.addWidget(self.ComPort)
        spacerItem = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.B_Open = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.B_Open.setCheckable(False)
        self.B_Open.setAutoDefault(False)
        self.B_Open.setDefault(False)
        self.B_Open.setFlat(False)
        self.B_Open.setObjectName(_fromUtf8("B_Open"))
        self.horizontalLayout.addWidget(self.B_Open)
        self.verticalLayoutWidget = QtGui.QWidget(GSMConfigurationUtility)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 90, 138, 201))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.B_DisableAutoBaud = QtGui.QPushButton(self.verticalLayoutWidget)
        self.B_DisableAutoBaud.setObjectName(_fromUtf8("B_DisableAutoBaud"))
        self.verticalLayout.addWidget(self.B_DisableAutoBaud)
        self.B_MsgFormat = QtGui.QPushButton(self.verticalLayoutWidget)
        self.B_MsgFormat.setObjectName(_fromUtf8("B_MsgFormat"))
        self.verticalLayout.addWidget(self.B_MsgFormat)
        self.PhNumber = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.PhNumber.setObjectName(_fromUtf8("PhNumber"))
        self.verticalLayout.addWidget(self.PhNumber)
        self.B_Call = QtGui.QPushButton(self.verticalLayoutWidget)
        self.B_Call.setObjectName(_fromUtf8("B_Call"))
        self.verticalLayout.addWidget(self.B_Call)
        self.B_halt = QtGui.QPushButton(self.verticalLayoutWidget)
        self.B_halt.setObjectName(_fromUtf8("B_halt"))
        self.verticalLayout.addWidget(self.B_halt)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(GSMConfigurationUtility)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(159, 89, 231, 201))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textLog = QtGui.QTextEdit(self.horizontalLayoutWidget_2)
        self.textLog.setLineWidth(5)
        self.textLog.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textLog.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textLog.setReadOnly(True)
        self.textLog.setObjectName(_fromUtf8("textLog"))
        self.horizontalLayout_2.addWidget(self.textLog)

        self.retranslateUi(GSMConfigurationUtility)
        QtCore.QObject.connect(self.ComPort, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.B_Open.animateClick)
        QtCore.QObject.connect(self.PhNumber, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.B_Call.animateClick)
        QtCore.QMetaObject.connectSlotsByName(GSMConfigurationUtility)
        GSMConfigurationUtility.setTabOrder(self.ComPort, self.B_Open)
        GSMConfigurationUtility.setTabOrder(self.B_Open, self.B_DisableAutoBaud)
        GSMConfigurationUtility.setTabOrder(self.B_DisableAutoBaud, self.B_MsgFormat)
        GSMConfigurationUtility.setTabOrder(self.B_MsgFormat, self.PhNumber)
        GSMConfigurationUtility.setTabOrder(self.PhNumber, self.B_halt)
        GSMConfigurationUtility.setTabOrder(self.B_halt, self.textLog)
        GSMConfigurationUtility.setTabOrder(self.textLog, self.B_Call)

    def retranslateUi(self, GSMConfigurationUtility):
        GSMConfigurationUtility.setWindowTitle(_translate("GSMConfigurationUtility", "GSM Configuration Utility", None))
        self.ComPort.setToolTip(_translate("GSMConfigurationUtility", "<html><head/><body><p>Enter Serial port Name</p><p>eg: /dev/ttyUSB0</p></body></html>", None))
        self.B_Open.setToolTip(_translate("GSMConfigurationUtility", "<html><head/><body><p>Open Comport</p></body></html>", None))
        self.B_Open.setText(_translate("GSMConfigurationUtility", "Open", None))
        self.B_DisableAutoBaud.setToolTip(_translate("GSMConfigurationUtility", "<html><head/><body><p>Disable Autobauding</p></body></html>", None))
        self.B_DisableAutoBaud.setText(_translate("GSMConfigurationUtility", "Disable AutoBauding", None))
        self.B_MsgFormat.setToolTip(_translate("GSMConfigurationUtility", "<html><head/><body><p>Set Text Message format</p></body></html>", None))
        self.B_MsgFormat.setText(_translate("GSMConfigurationUtility", "Set Msg Text Mode", None))
        self.PhNumber.setToolTip(_translate("GSMConfigurationUtility", "<html><head/><body><p>Type Phone number</p><p>eg: 8129025513</p></body></html>", None))
        self.B_Call.setToolTip(_translate("GSMConfigurationUtility", "<html><head/><body><p>Call specific number above</p></body></html>", None))
        self.B_Call.setText(_translate("GSMConfigurationUtility", "Call", None))
        self.B_halt.setToolTip(_translate("GSMConfigurationUtility", "<html><head/><body><p>End the call</p></body></html>", None))
        self.B_halt.setText(_translate("GSMConfigurationUtility", "Halt", None))
        self.textLog.setToolTip(_translate("GSMConfigurationUtility", "<html><head/><body><p>Logger</p></body></html>", None))

