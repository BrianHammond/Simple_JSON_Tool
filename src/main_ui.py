# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(865, 620)
        icon = QIcon()
        icon.addFile(u":/images/ms_icon.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.newFile_action = QAction(MainWindow)
        self.newFile_action.setObjectName(u"newFile_action")
        self.about_action = QAction(MainWindow)
        self.about_action.setObjectName(u"about_action")
        self.open_action = QAction(MainWindow)
        self.open_action.setObjectName(u"open_action")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_about_qt = QAction(MainWindow)
        self.action_about_qt.setObjectName(u"action_about_qt")
        self.action_dark_mode = QAction(MainWindow)
        self.action_dark_mode.setObjectName(u"action_dark_mode")
        self.action_dark_mode.setCheckable(True)
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_first_name = QLineEdit(self.groupBox)
        self.line_first_name.setObjectName(u"line_first_name")

        self.horizontalLayout_2.addWidget(self.line_first_name)

        self.line_middle_name = QLineEdit(self.groupBox)
        self.line_middle_name.setObjectName(u"line_middle_name")

        self.horizontalLayout_2.addWidget(self.line_middle_name)

        self.line_last_name = QLineEdit(self.groupBox)
        self.line_last_name.setObjectName(u"line_last_name")

        self.horizontalLayout_2.addWidget(self.line_last_name)

        self.line_age = QLineEdit(self.groupBox)
        self.line_age.setObjectName(u"line_age")

        self.horizontalLayout_2.addWidget(self.line_age)

        self.line_title = QLineEdit(self.groupBox)
        self.line_title.setObjectName(u"line_title")

        self.horizontalLayout_2.addWidget(self.line_title)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.line_address1 = QLineEdit(self.groupBox)
        self.line_address1.setObjectName(u"line_address1")

        self.horizontalLayout_5.addWidget(self.line_address1)

        self.line_address2 = QLineEdit(self.groupBox)
        self.line_address2.setObjectName(u"line_address2")

        self.horizontalLayout_5.addWidget(self.line_address2)

        self.line_country = QLineEdit(self.groupBox)
        self.line_country.setObjectName(u"line_country")

        self.horizontalLayout_5.addWidget(self.line_country)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.line_information = QLineEdit(self.groupBox)
        self.line_information.setObjectName(u"line_information")

        self.horizontalLayout_6.addWidget(self.line_information)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button_add = QPushButton(self.groupBox)
        self.button_add.setObjectName(u"button_add")

        self.horizontalLayout_4.addWidget(self.button_add)

        self.button_update = QPushButton(self.groupBox)
        self.button_update.setObjectName(u"button_update")

        self.horizontalLayout_4.addWidget(self.button_update)

        self.button_delete = QPushButton(self.groupBox)
        self.button_delete.setObjectName(u"button_delete")

        self.horizontalLayout_4.addWidget(self.button_delete)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addWidget(self.groupBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.filter_firstname = QLineEdit(self.groupBox_2)
        self.filter_firstname.setObjectName(u"filter_firstname")

        self.horizontalLayout_3.addWidget(self.filter_firstname)

        self.filter_lastname = QLineEdit(self.groupBox_2)
        self.filter_lastname.setObjectName(u"filter_lastname")

        self.horizontalLayout_3.addWidget(self.filter_lastname)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.button_filter = QPushButton(self.groupBox_2)
        self.button_filter.setObjectName(u"button_filter")

        self.verticalLayout.addWidget(self.button_filter)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.table = QTableWidget(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 865, 22))
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.line_first_name, self.line_middle_name)
        QWidget.setTabOrder(self.line_middle_name, self.line_last_name)
        QWidget.setTabOrder(self.line_last_name, self.line_age)
        QWidget.setTabOrder(self.line_age, self.line_title)
        QWidget.setTabOrder(self.line_title, self.line_address1)
        QWidget.setTabOrder(self.line_address1, self.line_address2)
        QWidget.setTabOrder(self.line_address2, self.line_country)
        QWidget.setTabOrder(self.line_country, self.line_information)
        QWidget.setTabOrder(self.line_information, self.button_add)
        QWidget.setTabOrder(self.button_add, self.button_update)
        QWidget.setTabOrder(self.button_update, self.button_delete)
        QWidget.setTabOrder(self.button_delete, self.filter_firstname)
        QWidget.setTabOrder(self.filter_firstname, self.filter_lastname)
        QWidget.setTabOrder(self.filter_lastname, self.button_filter)
        QWidget.setTabOrder(self.button_filter, self.table)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.action_about)
        self.menuHelp.addAction(self.action_about_qt)
        self.menuSettings.addAction(self.action_dark_mode)
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.action_open)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple JSON Tool", None))
        self.newFile_action.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.newFile_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.about_action.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.open_action.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.open_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_about_qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.action_dark_mode.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.action_new.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Employee Information", None))
        self.line_first_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.line_middle_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.line_last_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.line_age.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.line_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.line_address1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address 1", None))
        self.line_address2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address 2", None))
        self.line_country.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Country", None))
        self.line_information.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Additional Information", None))
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_update.setText(QCoreApplication.translate("MainWindow", u"Update Info", None))
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"Delete Entry", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.filter_firstname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter First Name", None))
        self.filter_lastname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter Last Name", None))
        self.button_filter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

