__author__ = 'kuba'

import sys
import main_window_ui
from PyQt4 import QtGui
from PyQt4 import QtCore
import serial.tools.list_ports


class main_window(QtGui.QMainWindow):
    def __init__(self):
        super(QtGui.QMainWindow, self).__init__(None)
        self._ui = main_window_ui.Ui_MainWindow()
        self._ui.setupUi(self)

        # scan serial port
        self._scan_serial_ports()

        self._tmr = QtCore.QTimer()
        self._tmr.timeout.connect(self._timer_slot)
        self._tmr.setInterval(50)

        self._ui.pb_connect.clicked.connect(self.pb_connect_slot)
        self._ui.pb_disconnect.clicked.connect(self.pb_disconnect_slot),
        self._ui.pb_stop.clicked.connect(self.pb_stop)

        self.widget_connection()

        self._ui.sl_left.setAttribute(QtCore.Qt.WA_AcceptTouchEvents)
        self._ui.sl_right.setAttribute(QtCore.Qt.WA_AcceptTouchEvents)


    def pb_stop(self):
        self._ui.sl_left.setValue(0)
        self._ui.sl_right.setValue(0)

    def widget_connection(self):
        try:
            op = self._com.isOpen()
        except:
            op = False
        self._ui.pb_connect.setDisabled(op)
        self._ui.pb_disconnect.setEnabled(op)

    def pb_connect_slot(self):
        self._connect_port(True)
        self.widget_connection()
        pass

    def pb_disconnect_slot(self):
        self._connect_port(False)
        self.widget_connection()
        pass

    def __del__(self):
        try:
            self._settings.setValue("main/com",self._ui.cmb_com.currentText())
            #self._settings.setValue("main/last_path",self._path)
            self._com.close()
        except:
            pass

    def _connect_port(self,connect):
        if connect:
            try:
                name = self._ui.cmb_com.currentText()
                self._com = serial.Serial(str(name),9600,timeout = 1)
                self._ui.statusbar.showMessage(self.tr("pripojeno ke com portu"))
                self._tmr.start()
            except:
                self._ui.statusbar.showMessage(self.tr("nemuzu pripojit com port"))
                self._tmr.stop()
                pass
        else:
            try:

                self._com.close()
                self._tmr.stop()
                self._ui.statusbar.showMessage(self.tr("Odpojeno od com portu"))
            except:
                self._tmr.stop()
                pass

    def _timer_slot(self):
        try:
            #vytvorit slovo rychlosti a smeru a poslat
            lst = []
            lst.append(self._ui.sl_left.value())
            lst.append(self._ui.sl_right.value())

            wr = "\xfd\xef"
            for a in lst:
                value = abs(a)
                sign = 0;
                if a < 0:
                    sign = 1

                wr += chr(sign)
                value = value * 100
                wr += chr(value / 256)
                wr += chr(value % 256)

            wr += "\xfa\xfc"
            print wr.encode("hex")
            #self._ui.pte_log.appendPlainText(wr.encode("hex"))
            self._com.write(wr)

        except:
            pass

    def _scan_serial_ports(self):
        st = serial.tools.list_ports.comports()
        self._ui.cmb_com.clear()

        lst = []
        for a in st:
            lst.append(a[0])

        self._ui.cmb_com.addItems(lst)
        pass




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mw = main_window()
    mw.show()
    app.exec_()







