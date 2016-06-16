# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-jpeg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1318, 770)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 631, 601))
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox::title {\n"
"  color: rgb(102, 137, 153)\n"
"}\n"
"\n"
"QGroupBox::border {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"    background-color:transparent;\n"
"      border: 2px groove rgb(102, 137, 153) ;\n"
"    border-radius: 0px\n"
"}"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.graphicsView = QtGui.QGraphicsView(self.groupBox_2)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 591, 561))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(670, 20, 631, 601))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox::title {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"QGroupBox::border {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"    background-color:transparent;\n"
"      border: 2px groove rgb(255, 94, 94); ;\n"
"    border-radius: 0px\n"
"}"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.groupBox)
        self.graphicsView_2.setGeometry(QtCore.QRect(20, 20, 591, 561))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(790, 630, 511, 101))
        self.groupBox_3.setStyleSheet(_fromUtf8("QGroupBox::title {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"QGroupBox::border {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"    background-color:transparent;\n"
"      border: 2px groove rgb(255, 94, 94); ;\n"
"    border-radius: 0px\n"
"}"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.quality = phonon.Phonon.SeekSlider(self.groupBox_3)
        self.quality.setGeometry(QtCore.QRect(10, 30, 481, 22))
        self.quality.setIconVisible(True)
        self.quality.setProperty("1", 1)
        self.quality.setProperty("2", 2)
        self.quality.setProperty("3", 3)
        self.quality.setProperty("4", 4)
        self.quality.setProperty("5", 5)
        self.quality.setProperty("6", 6)
        self.quality.setProperty("7", 7)
        self.quality.setProperty("8", 8)
        self.quality.setProperty("9", 9)
        self.quality.setObjectName(_fromUtf8("quality"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(210, 60, 41, 31))
        self.plainTextEdit_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;"))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(670, 630, 111, 101))
        self.groupBox_4.setStyleSheet(_fromUtf8("QGroupBox::title {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"QGroupBox::border {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"    background-color:transparent;\n"
"      border: 2px groove rgb(255, 94, 94); ;\n"
"    border-radius: 0px\n"
"}"))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 91, 31))
        self.plainTextEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;"))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton = QtGui.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(40, 60, 31, 26))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"text-color:black;\n"
"background-color: white;\n"
"border-width: 1px;\n"
"border-color: gray;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 12px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 640, 101, 71))
        self.groupBox_5.setStyleSheet(_fromUtf8("QGroupBox::title {\n"
"  color: rgb(102, 137, 153)\n"
"}\n"
"\n"
"QGroupBox::border {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"    background-color:transparent;\n"
"      border: 2px groove rgb(102, 137, 153) ;\n"
"    border-radius: 0px\n"
"}"))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 30, 81, 26))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"text-color:black;\n"
"background-color: white;\n"
"border-width: 1px;\n"
"border-color: gray;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 12px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"\n"
"}"))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox_2.setTitle(_translate("Form", "Original Image", None))
        self.groupBox.setTitle(_translate("Form", "DCT2", None))
        self.groupBox_3.setTitle(_translate("Form", "Quality", None))
        self.groupBox_4.setTitle(_translate("Form", "N", None))
        self.pushButton.setText(_translate("Form", "OK", None))
        self.groupBox_5.setTitle(_translate("Form", "Open file", None))
        self.pushButton_2.setText(_translate("Form", "Open file", None))

from PyQt4 import phonon

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

