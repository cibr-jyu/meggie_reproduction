# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runActionsDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RunActionsDialog(object):
    def setupUi(self, RunActionsDialog):
        RunActionsDialog.setObjectName("RunActionsDialog")
        RunActionsDialog.setWindowModality(QtCore.Qt.NonModal)
        RunActionsDialog.resize(777, 783)
        self.gridLayout = QtWidgets.QGridLayout(RunActionsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_10.addItem(spacerItem)
        self.pushButtonClose = QtWidgets.QPushButton(RunActionsDialog)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout_10.addWidget(self.pushButtonClose)
        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(RunActionsDialog)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 759, 734))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout_7.addItem(spacerItem1, 3, 0, 1, 1)
        self.groupBoxSource = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxSource.setObjectName("groupBoxSource")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBoxSource)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelSourceBrowse = QtWidgets.QLabel(self.groupBoxSource)
        self.labelSourceBrowse.setObjectName("labelSourceBrowse")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.labelSourceBrowse
        )
        self.pushButtonSourceBrowse = QtWidgets.QPushButton(self.groupBoxSource)
        self.pushButtonSourceBrowse.setObjectName("pushButtonSourceBrowse")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.pushButtonSourceBrowse
        )
        self.labelBrowseCurrentSelectionLabel = QtWidgets.QLabel(self.groupBoxSource)
        self.labelBrowseCurrentSelectionLabel.setObjectName(
            "labelBrowseCurrentSelectionLabel"
        )
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.labelBrowseCurrentSelectionLabel
        )
        self.labelBrowseCurrentSelectionFilename = QtWidgets.QLabel(self.groupBoxSource)
        self.labelBrowseCurrentSelectionFilename.setText("")
        self.labelBrowseCurrentSelectionFilename.setObjectName(
            "labelBrowseCurrentSelectionFilename"
        )
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.labelBrowseCurrentSelectionFilename
        )
        self.gridLayout_7.addWidget(self.groupBoxSource, 0, 0, 1, 1)
        self.groupBoxSubject = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxSubject.setObjectName("groupBoxSubject")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBoxSubject)
        self.formLayout_3.setObjectName("formLayout_3")
        self.labelSubject = QtWidgets.QLabel(self.groupBoxSubject)
        self.labelSubject.setObjectName("labelSubject")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.labelSubject
        )
        self.comboBoxSubject = QtWidgets.QComboBox(self.groupBoxSubject)
        self.comboBoxSubject.setObjectName("comboBoxSubject")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.comboBoxSubject
        )
        self.gridLayout_7.addWidget(self.groupBoxSubject, 1, 0, 1, 1)
        self.groupBoxActions = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxActions.setObjectName("groupBoxActions")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxActions)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelActionsAvailable = QtWidgets.QLabel(self.groupBoxActions)
        self.labelActionsAvailable.setObjectName("labelActionsAvailable")
        self.gridLayout_2.addWidget(self.labelActionsAvailable, 0, 0, 1, 1)
        self.textBrowserActionsInfo = QtWidgets.QTextBrowser(self.groupBoxActions)
        self.textBrowserActionsInfo.setObjectName("textBrowserActionsInfo")
        self.gridLayout_2.addWidget(self.textBrowserActionsInfo, 1, 1, 4, 1)
        self.listWidgetAvailable = QtWidgets.QListWidget(self.groupBoxActions)
        self.listWidgetAvailable.setObjectName("listWidgetAvailable")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetAvailable.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetAvailable.addItem(item)
        self.gridLayout_2.addWidget(self.listWidgetAvailable, 1, 0, 1, 1)
        self.pushButtonActionsRun = QtWidgets.QPushButton(self.groupBoxActions)
        self.pushButtonActionsRun.setObjectName("pushButtonActionsRun")
        self.gridLayout_2.addWidget(self.pushButtonActionsRun, 2, 0, 1, 1)
        self.listWidgetDone = QtWidgets.QListWidget(self.groupBoxActions)
        self.listWidgetDone.setObjectName("listWidgetDone")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDone.addItem(item)
        self.gridLayout_2.addWidget(self.listWidgetDone, 4, 0, 1, 1)
        self.labelActionsDone = QtWidgets.QLabel(self.groupBoxActions)
        self.labelActionsDone.setObjectName("labelActionsDone")
        self.gridLayout_2.addWidget(self.labelActionsDone, 3, 0, 1, 1)
        self.labelActionsInfo = QtWidgets.QLabel(self.groupBoxActions)
        self.labelActionsInfo.setObjectName("labelActionsInfo")
        self.gridLayout_2.addWidget(self.labelActionsInfo, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBoxActions, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(RunActionsDialog)
        QtCore.QMetaObject.connectSlotsByName(RunActionsDialog)

    def retranslateUi(self, RunActionsDialog):
        _translate = QtCore.QCoreApplication.translate
        RunActionsDialog.setWindowTitle(
            _translate("RunActionsDialog", "Meggie - Run Actions from Log")
        )
        self.pushButtonClose.setText(_translate("RunActionsDialog", "Close"))
        self.groupBoxSource.setTitle(_translate("RunActionsDialog", "Source"))
        self.labelSourceBrowse.setText(
            _translate("RunActionsDialog", "Select the action log:")
        )
        self.pushButtonSourceBrowse.setText(_translate("RunActionsDialog", "Browse..."))
        self.labelBrowseCurrentSelectionLabel.setText(
            _translate("RunActionsDialog", "Current selection:")
        )
        self.groupBoxSubject.setTitle(_translate("RunActionsDialog", "Subject"))
        self.labelSubject.setText(_translate("RunActionsDialog", "Based on subject:"))
        self.groupBoxActions.setTitle(_translate("RunActionsDialog", "Actions"))
        self.labelActionsAvailable.setText(
            _translate("RunActionsDialog", "Available actions:")
        )
        self.textBrowserActionsInfo.setHtml(
            _translate(
                "RunActionsDialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;cat&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;dog,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;elephant&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;raw&quot;</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;meow&quot;</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;tsuk&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;tsok&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;tsek&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;tsik&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;tsuk&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;,</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  &quot;&quot;</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">}</p></body></html>',
            )
        )
        __sortingEnabled = self.listWidgetAvailable.isSortingEnabled()
        self.listWidgetAvailable.setSortingEnabled(False)
        item = self.listWidgetAvailable.item(0)
        item.setText(_translate("RunActionsDialog", "Another cat"))
        item = self.listWidgetAvailable.item(1)
        item.setText(_translate("RunActionsDialog", "Another mindless human"))
        self.listWidgetAvailable.setSortingEnabled(__sortingEnabled)
        self.pushButtonActionsRun.setText(
            _translate("RunActionsDialog", "Run selected action")
        )
        __sortingEnabled = self.listWidgetDone.isSortingEnabled()
        self.listWidgetDone.setSortingEnabled(False)
        item = self.listWidgetDone.item(0)
        item.setText(_translate("RunActionsDialog", "Cat"))
        item = self.listWidgetDone.item(1)
        item.setText(_translate("RunActionsDialog", "Bird"))
        item = self.listWidgetDone.item(2)
        item.setText(_translate("RunActionsDialog", "Fly"))
        item = self.listWidgetDone.item(3)
        item.setText(_translate("RunActionsDialog", "Frog"))
        item = self.listWidgetDone.item(4)
        item.setText(_translate("RunActionsDialog", "Lion"))
        item = self.listWidgetDone.item(5)
        item.setText(_translate("RunActionsDialog", "Hippo"))
        item = self.listWidgetDone.item(6)
        item.setText(_translate("RunActionsDialog", "Another cat"))
        item = self.listWidgetDone.item(7)
        item.setText(_translate("RunActionsDialog", "Eagle"))
        item = self.listWidgetDone.item(8)
        item.setText(_translate("RunActionsDialog", "Giraffe"))
        item = self.listWidgetDone.item(9)
        item.setText(_translate("RunActionsDialog", "Bird"))
        item = self.listWidgetDone.item(10)
        item.setText(_translate("RunActionsDialog", "Crocodile"))
        item = self.listWidgetDone.item(11)
        item.setText(_translate("RunActionsDialog", "Zen master"))
        item = self.listWidgetDone.item(12)
        item.setText(_translate("RunActionsDialog", "Dog"))
        item = self.listWidgetDone.item(13)
        item.setText(_translate("RunActionsDialog", "Fox"))
        item = self.listWidgetDone.item(14)
        item.setText(_translate("RunActionsDialog", "Wolf"))
        item = self.listWidgetDone.item(15)
        item.setText(_translate("RunActionsDialog", "Raven"))
        item = self.listWidgetDone.item(16)
        item.setText(_translate("RunActionsDialog", "Ninetales"))
        self.listWidgetDone.setSortingEnabled(__sortingEnabled)
        self.labelActionsDone.setText(_translate("RunActionsDialog", "Done:"))
        self.labelActionsInfo.setText(_translate("RunActionsDialog", "Info:"))
