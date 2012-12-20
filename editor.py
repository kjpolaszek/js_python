# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created: Thu Dec 20 03:31:09 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_editor(object):
    def setupUi(self, editor):
        editor.setObjectName(_fromUtf8("editor"))
        editor.resize(555, 470)
        editor.setMinimumSize(QtCore.QSize(555, 470))
        self.centralwidget = QtGui.QWidget(editor)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 501, 351))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textEdit = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 2, 2, 1, 1)
        self.listView = QtGui.QListView(self.gridLayoutWidget)
        self.listView.setMaximumSize(QtCore.QSize(158, 16777215))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout_2.addWidget(self.listView, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.label_date = QtGui.QLabel(self.gridLayoutWidget)
        self.label_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_date.setObjectName(_fromUtf8("label_date"))
        self.gridLayout_2.addWidget(self.label_date, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        editor.setCentralWidget(self.gridLayoutWidget)
        self.menubar = QtGui.QMenuBar(editor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 555, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuPlik = QtGui.QMenu(self.menubar)
        self.menuPlik.setObjectName(_fromUtf8("menuPlik"))
        self.menuPomoc = QtGui.QMenu(self.menubar)
        self.menuPomoc.setObjectName(_fromUtf8("menuPomoc"))
        self.menuEdycja = QtGui.QMenu(self.menubar)
        self.menuEdycja.setObjectName(_fromUtf8("menuEdycja"))
        editor.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(editor)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        editor.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(editor)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        editor.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClear = QtGui.QAction(editor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/clear_document-icon.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionOpen = QtGui.QAction(editor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/open_256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(editor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/Save-as-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(editor)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionHelp = QtGui.QAction(editor)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionInfo = QtGui.QAction(editor)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionSave_as = QtGui.QAction(editor)
        self.actionSave_as.setIcon(icon2)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionRemove = QtGui.QAction(editor)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/Document-Delete-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove.setIcon(icon4)
        self.actionRemove.setObjectName(_fromUtf8("actionRemove"))
        self.actionnew_day = QtGui.QAction(editor)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/document_add_256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionnew_day.setIcon(icon5)
        self.actionnew_day.setObjectName(_fromUtf8("actionnew_day"))
        self.menuPlik.addAction(self.actionnew_day)
        self.menuPlik.addSeparator()
        self.menuPlik.addAction(self.actionOpen)
        self.menuPlik.addAction(self.actionSave)
        self.menuPlik.addAction(self.actionSave_as)
        self.menuPlik.addSeparator()
        self.menuPlik.addAction(self.actionExit)
        self.menuPomoc.addAction(self.actionHelp)
        self.menuPomoc.addSeparator()
        self.menuPomoc.addAction(self.actionInfo)
        self.menuEdycja.addAction(self.actionClear)
        self.menuEdycja.addAction(self.actionRemove)
        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuEdycja.menuAction())
        self.menubar.addAction(self.menuPomoc.menuAction())
        self.toolBar.addAction(self.actionnew_day)
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addAction(self.actionRemove)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(editor)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), editor.close)
        QtCore.QMetaObject.connectSlotsByName(editor)

    def retranslateUi(self, editor):
        editor.setWindowTitle(QtGui.QApplication.translate("editor", "Pamiętnik", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("editor", "Wybierz dzień", None, QtGui.QApplication.UnicodeUTF8))
        self.label_date.setText(QtGui.QApplication.translate("editor", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("editor", "Zawartość:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlik.setTitle(QtGui.QApplication.translate("editor", "Plik", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPomoc.setTitle(QtGui.QApplication.translate("editor", "Pomoc", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdycja.setTitle(QtGui.QApplication.translate("editor", "Edycja", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("editor", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("editor", "&Wyczyść", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setToolTip(QtGui.QApplication.translate("editor", "Usuwa Cały Tekst", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setShortcut(QtGui.QApplication.translate("editor", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("editor", "&Otwórz", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setToolTip(QtGui.QApplication.translate("editor", "Otwiera plik", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("editor", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("editor", "&Zapisz", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("editor", "Zapisuje plik", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("editor", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("editor", "Zakończ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("editor", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("editor", "Pomoc Pamiętnik", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInfo.setText(QtGui.QApplication.translate("editor", "Informacje o ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("editor", "Zapisz j&ako...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setShortcut(QtGui.QApplication.translate("editor", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove.setText(QtGui.QApplication.translate("editor", "Usuń wpis!", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove.setToolTip(QtGui.QApplication.translate("editor", "Usuwa dany wpis", None, QtGui.QApplication.UnicodeUTF8))
        self.actionnew_day.setText(QtGui.QApplication.translate("editor", "Nowy Dzień", None, QtGui.QApplication.UnicodeUTF8))
        self.actionnew_day.setToolTip(QtGui.QApplication.translate("editor", "Tworzy nowy wpis z dzisiejszą datą", None, QtGui.QApplication.UnicodeUTF8))

