# Form implementation generated from reading ui file 'UI_Files/applied_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(207, 177)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.applied_frame = QtWidgets.QFrame(parent=Form)
        self.applied_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.applied_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.applied_frame.setObjectName("applied_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.applied_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gif = QtWidgets.QLabel(parent=self.applied_frame)
        self.gif.setMaximumSize(QtCore.QSize(100000, 100000))
        self.gif.setText("")
        self.gif.setScaledContents(True)
        self.gif.setObjectName("gif")
        self.verticalLayout_2.addWidget(self.gif)
        self.applied_text = QtWidgets.QLabel(parent=self.applied_frame)
        self.applied_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.applied_text.setObjectName("applied_text")
        self.verticalLayout_2.addWidget(self.applied_text)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_button = QtWidgets.QPushButton(parent=self.applied_frame)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.applied_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.applied_text.setText(_translate("Form", "Changes Applied"))
        self.ok_button.setText(_translate("Form", "OK"))
