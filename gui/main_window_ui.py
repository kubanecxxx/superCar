# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Tue Jul 07 13:54:30 2015
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(_fromUtf8("\n"
"\n"
"QSlider::handle\n"
"{\n"
" background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
" border: 1px solid #5c5c5c;\n"
" border-radius: 3px;\n"
"\n"
" height: 100px;\n"
"}\n"
"\n"
"QSlider::groove\n"
"{\n"
" border: 1px solid #999999;\n"
" background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #E6E6E6, stop:1 #EEEEEE);\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_auto = QtGui.QWidget()
        self.tab_auto.setObjectName(_fromUtf8("tab_auto"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_auto)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pb_stop = QtGui.QPushButton(self.tab_auto)
        self.pb_stop.setMinimumSize(QtCore.QSize(0, 48))
        self.pb_stop.setIconSize(QtCore.QSize(16, 16))
        self.pb_stop.setObjectName(_fromUtf8("pb_stop"))
        self.verticalLayout_3.addWidget(self.pb_stop)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.tab_auto)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_6 = QtGui.QLabel(self.tab_auto)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.tab_auto)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(self.tab_auto)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.sl_left = QtGui.QSlider(self.tab_auto)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sl_left.sizePolicy().hasHeightForWidth())
        self.sl_left.setSizePolicy(sizePolicy)
        self.sl_left.setMinimum(-100)
        self.sl_left.setMaximum(100)
        self.sl_left.setOrientation(QtCore.Qt.Vertical)
        self.sl_left.setObjectName(_fromUtf8("sl_left"))
        self.gridLayout.addWidget(self.sl_left, 2, 0, 1, 1)
        self.sl_right = QtGui.QSlider(self.tab_auto)
        self.sl_right.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sl_right.sizePolicy().hasHeightForWidth())
        self.sl_right.setSizePolicy(sizePolicy)
        self.sl_right.setMinimum(-100)
        self.sl_right.setMaximum(100)
        self.sl_right.setOrientation(QtCore.Qt.Vertical)
        self.sl_right.setObjectName(_fromUtf8("sl_right"))
        self.gridLayout.addWidget(self.sl_right, 2, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_auto, _fromUtf8(""))
        self.tab_com = QtGui.QWidget()
        self.tab_com.setObjectName(_fromUtf8("tab_com"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_com)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.tab_com)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.cmb_com = QtGui.QComboBox(self.tab_com)
        self.cmb_com.setObjectName(_fromUtf8("cmb_com"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cmb_com)
        self.label_2 = QtGui.QLabel(self.tab_com)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.chk_autostop = QtGui.QCheckBox(self.tab_com)
        self.chk_autostop.setText(_fromUtf8(""))
        self.chk_autostop.setObjectName(_fromUtf8("chk_autostop"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.chk_autostop)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.pte_log = QtGui.QPlainTextEdit(self.tab_com)
        self.pte_log.setReadOnly(True)
        self.pte_log.setObjectName(_fromUtf8("pte_log"))
        self.verticalLayout_2.addWidget(self.pte_log)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pb_connect = QtGui.QPushButton(self.tab_com)
        self.pb_connect.setObjectName(_fromUtf8("pb_connect"))
        self.horizontalLayout.addWidget(self.pb_connect)
        self.pb_disconnect = QtGui.QPushButton(self.tab_com)
        self.pb_disconnect.setObjectName(_fromUtf8("pb_disconnect"))
        self.horizontalLayout.addWidget(self.pb_disconnect)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_com, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.sl_left, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_5.setNum)
        QtCore.QObject.connect(self.sl_right, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_6.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pb_stop.setText(_translate("MainWindow", "Stop", None))
        self.label_4.setText(_translate("MainWindow", "Pravý pás", None))
        self.label_6.setText(_translate("MainWindow", "0", None))
        self.label_3.setText(_translate("MainWindow", "Levý pás", None))
        self.label_5.setText(_translate("MainWindow", "0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_auto), _translate("MainWindow", "Auto", None))
        self.label.setText(_translate("MainWindow", "Comport", None))
        self.label_2.setText(_translate("MainWindow", "Automaticky zastavit", None))
        self.pb_connect.setText(_translate("MainWindow", "Připojit", None))
        self.pb_disconnect.setText(_translate("MainWindow", "Odpojit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_com), _translate("MainWindow", "Setup", None))

