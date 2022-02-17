import sys
import cluster
import evaluation_measures
import expansion_query
import model
import glob
import os
import json
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import  QFileDialog, QWidget, QTableWidgetItem
from PyQt5.QtWidgets import  QCheckBox, QHBoxLayout



class Ui_MainWindow(object):
    
    def __init__(self):
        self.build = False

    '''Construimos los botones, los cuadros de texto, etc'''
    def setupUi (self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366,768)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.HBoxLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.HBoxLayout.setObjectName("HBoxLayout")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_16 = QtWidgets.QFrame(self.groupBox_7)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_select_directory = QtWidgets.QLineEdit(self.frame_16)
        self.lineEdit_select_directory.setObjectName("lineEdit_select_directory")
        self.horizontalLayout_5.addWidget(self.lineEdit_select_directory)
        self.toolButton_select_directory = QtWidgets.QToolButton(self.frame_16)
        self.toolButton_select_directory.setObjectName("toolButton_select_directory")
        self.horizontalLayout_5.addWidget(self.toolButton_select_directory)
        self.verticalLayout_13.addWidget(self.frame_16)
        self.indexing_label = QtWidgets.QLabel(self.groupBox_7)
        self.indexing_label.setText("")
        self.indexing_label.setObjectName("indexing_label")
        self.verticalLayout_13.addWidget(self.indexing_label)
        self.verticalLayout_9.addWidget(self.groupBox_7)
        self.frame_8 = QtWidgets.QFrame(self.tab_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_8)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_query = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_query.setObjectName("lineEdit_query")
        self.verticalLayout_8.addWidget(self.lineEdit_query)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_query = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_query.setObjectName("pushButton_query")
        self.gridLayout.addWidget(self.pushButton_query, 1, 2, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_2)
        self.label_query = QtWidgets.QLabel(self.groupBox_2)
        self.label_query.setText("")
        self.label_query.setObjectName("label_query")
        self.verticalLayout_8.addWidget(self.label_query)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.frame = QtWidgets.QFrame(self.frame_8)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.Results = QtWidgets.QWidget()
        self.Results.setObjectName("Results")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Results)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.Results)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget_results = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget_results.setObjectName("tableWidget_results")
        self.tableWidget_results.setColumnCount(2)
        self.tableWidget_results.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_results.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_results.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.tableWidget_results)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.tabWidget.addTab(self.Results, "")
        self.SelectRelevantDocument = QtWidgets.QWidget()
        self.SelectRelevantDocument.setObjectName("SelectRelevantDocument")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.SelectRelevantDocument)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.SelectRelevantDocument)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget_relevant = QtWidgets.QTableWidget(self.frame_5)
        self.tableWidget_relevant.setObjectName("tableWidget_relevant")
        self.tableWidget_relevant.setColumnCount(2)
        self.tableWidget_relevant.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_relevant.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_relevant.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_3.addWidget(self.tableWidget_relevant)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.tabWidget.addTab(self.SelectRelevantDocument, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame_3)
        
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_9.addWidget(self.frame_8)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.HBoxLayout.addWidget(self.tabWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        '''Mandamos a ejecutar los metodos en dependencia de lo que se seleccione'''
        self.retranslateUi(MainWindow)
        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        self.toolButton_select_directory.clicked.connect(self.selectDirectory)
        self.pushButton_query.clicked.connect(self.make_query)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget_2, self.lineEdit_select_directory)
        MainWindow.setTabOrder(self.lineEdit_select_directory, self.toolButton_select_directory)
        MainWindow.setTabOrder(self.tableWidget_relevant, self.tabWidget)
        
    '''Le damos nombre a los botones, los cuadros de texto,etc'''
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SRI"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Documents"))
        self.toolButton_select_directory.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Query"))
        self.pushButton_query.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Results), _translate("MainWindow", "Results"))
        item = self.tableWidget_results.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cluster"))
        item = self.tableWidget_results.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Document"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SelectRelevantDocument), _translate("MainWindow", "Documents"))
        item = self.tableWidget_relevant.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cluster"))
        item = self.tableWidget_relevant.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Document"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "SRI."))   

    '''Si damos clic en seleccionar el directorio'''
    def selectDirectory(self):
        self.indexing_label.setText("Processing documents")
        path = str(QFileDialog.getExistingDirectory())

        self.lineEdit_select_directory.setText(path)
        self.build_model(path)

    '''Si seleccionamos un directorio mandamos a procesar los documentos de este'''    
    def build_model(self,path):

        if not self.lineEdit_select_directory.text() == '':
            self.build = True
        
            docs = glob.glob(os.path.join(path + "/**", "*.txt"), recursive=True)
        
            cluster.clustering(path+"/",4)

            for i in reversed(range(self.tableWidget_relevant.rowCount())):
                self.tableWidget_relevant.removeRow(i)
            for item in range(len(docs)):
                row_position = self.tableWidget_relevant.rowCount()

                qwidget = QWidget()
                checkbox = QCheckBox()
                checkbox.setChecked(False)

                qhboxlayout = QHBoxLayout(qwidget)
                qhboxlayout.addWidget(checkbox)
                qhboxlayout.setContentsMargins(0, 0, 0, 0)
                name = os.path.basename(docs[item])
                self.tableWidget_relevant.insertRow(row_position)
                self.tableWidget_relevant.setItem(row_position, 0, QTableWidgetItem(cluster.all_label_from_cluster(name)))
                self.tableWidget_relevant.setItem(row_position, 1, QTableWidgetItem(name))

            self.disable_buttons()

            json_value = json.dumps({'action': 'build', 'path': path})

            model.model(json_value)

            self.enable_buttons()
            self.indexing_label.setText("")

    '''Para apagar los botones mientras se este procesando algo'''
    def disable_buttons(self):
        self.toolButton_select_directory.setEnabled(False)
        self.pushButton_query.setEnabled(False)
        self.lineEdit_query.setEnabled(False)

    '''Para encender los botones'''
    def enable_buttons(self):
        self.toolButton_select_directory.setEnabled(True)
        self.pushButton_query.setEnabled(True)
        self.lineEdit_query.setEnabled(True)

    '''Para procesar la consulta'''
    def make_query(self):
        if self.lineEdit_query.text() != "" and self.build:

            for i in reversed(range(self.tableWidget_results.rowCount())):
                self.tableWidget_results.removeRow(i)
            query = self.lineEdit_query.text()

            self.disable_buttons()
            self.label_query.setText("execcuting query")

            json_value = json.dumps({'action': 'query', 'query': query, 'umbral': 0.1})

            json_result = json.loads(expansion_query.start(json_value))

            for pair in json_result['results']:
                row_position = self.tableWidget_results.rowCount()
                print(type(row_position))
                self.tableWidget_results.insertRow(row_position)

                self.tableWidget_results.setItem(row_position, 0, QTableWidgetItem(cluster.all_label_from_cluster(str(pair["document"]))))
                self.tableWidget_results.setItem(row_position, 1, QTableWidgetItem(str(pair["document"])))

            self.enable_buttons()
            self.label_query.setText("")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
