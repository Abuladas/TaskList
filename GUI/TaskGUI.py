
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.DeleteItems_PB = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())

        self.DeleteItems_PB.setGeometry(QtCore.QRect(20, 110, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteItems_PB.setFont(font)
        self.DeleteItems_PB.setObjectName("DeleteItems_PB")
        self.Clearitems_PB = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Clear_it())
        self.Clearitems_PB.setGeometry(QtCore.QRect(20, 180, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Clearitems_PB.setFont(font)
        self.Clearitems_PB.setObjectName("Clearitems_PB")

        self.AddItems_PB = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_it())

        self.AddItems_PB.setGeometry(QtCore.QRect(20, 50, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddItems_PB.setFont(font)
        self.AddItems_PB.setObjectName("AddItems_PB")
        self.labelInput = QtWidgets.QLabel(self.centralwidget)
        self.labelInput.setGeometry(QtCore.QRect(230, 380, 551, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelInput.setFont(font)
        self.labelInput.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInput.setObjectName("labelInput")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 440, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.my_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.my_listWidget.setGeometry(QtCore.QRect(230, 51, 561, 321))
        self.my_listWidget.setObjectName("my_listWidget")
        self.labelCrrntTask = QtWidgets.QLabel(self.centralwidget)
        self.labelCrrntTask.setGeometry(QtCore.QRect(230, 0, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCrrntTask.setFont(font)
        self.labelCrrntTask.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCrrntTask.setObjectName("labelCrrntTask")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 520, 111, 41))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.actionLoad.triggered.connect(lambda: self.LoadFile())
        self.actionSave.triggered.connect(lambda: self.save())
        self.statusbar.setFont(QFont('Helvetica', 16))
        self.statusbar.showMessage("App has started successfully")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #remove tasks
    def remove_it(self):
        clicked= self.my_listWidget.currentRow()
        self.my_listWidget.takeItem(clicked)
        self.statusbar.showMessage("Selected Task have been removed")
        self.lineEdit.setText("")

    #clear tasks
    def Clear_it(self):
        self.my_listWidget.clear()
        self.statusbar.showMessage("All tasks have been cleared!")

    #add tasks
    def add_it(self):
        task= self.lineEdit.text()
        if task=="":
            return

        self.my_listWidget.addItem(task)
        self.statusbar.showMessage("The Task has been added!")
        self.lineEdit.setText("")





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task List App"))
        self.DeleteItems_PB.setText(_translate("MainWindow", "Remove a task"))
        self.Clearitems_PB.setText(_translate("MainWindow", "Clear all tasks"))
        self.AddItems_PB.setText(_translate("MainWindow", "Add a task"))
        self.labelInput.setText(_translate("MainWindow", "Text input:"))
        self.labelCrrntTask.setText(_translate("MainWindow", "Current Tasks"))
        self.label.setText(_translate("MainWindow", "By Sarey Abuladas"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+L"))


    def save(self):

        self.statusbar.showMessage("The Task list has been saved!")

    def LoadFile(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "Data files (*.txt)")
        if fname:

            tasks = load_from_file(fname)


            self.statusbar.showMessage("List loaded successfully:")







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
