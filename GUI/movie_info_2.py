# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie_info_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QMenu
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QDialog

from PyQt5.QtGui import QIcon

x, y = 0, 0


class movie_info_2(QDialog):
    def __init__(self):
        super(movie_info_2, self).__init__()
        self.setupUi()
        self.count = 0

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(835, 609)
        self.setStyleSheet("#Dialog{border-image:url(C:/Users/xiaoqi/Documents/Python_Spider_mysql/images/movie_bg.jpg)}")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(30, 10, 771, 581))
        self.widget.setObjectName("widget")
        self.jpg_label = QtWidgets.QLabel(self.widget)
        self.jpg_label.setGeometry(QtCore.QRect(10, 10, 208, 300))
        self.jpg_label.setObjectName("jpg_label")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(240, 10, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(240, 40, 45, 15))
        self.label_2.setMinimumSize(QtCore.QSize(25, 0))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(240, 70, 35, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(240, 100, 35, 15))
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(240, 130, 35, 15))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(240, 160, 35, 15))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(240, 190, 72, 15))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(240, 220, 35, 15))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(240, 250, 37, 15))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(20, 310, 100, 50))
        self.label_14.setTextFormat(QtCore.Qt.AutoText)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setGeometry(QtCore.QRect(580, 0, 150, 100))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setGeometry(QtCore.QRect(60, 360, 650, 170))
        self.label_16.setObjectName("label_16")
        self.label_16.setWordWrap(True)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setGeometry(QtCore.QRect(320, 10, 250, 15))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setGeometry(QtCore.QRect(290, 40, 151, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setGeometry(QtCore.QRect(290, 70, 281, 16))
        self.label_19.setObjectName("label_19")
        self.label_35 = QtWidgets.QLabel(self.widget)
        self.label_35.setGeometry(QtCore.QRect(290, 100, 271, 16))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.widget)
        self.label_36.setGeometry(QtCore.QRect(290, 130, 291, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.widget)
        self.label_37.setGeometry(QtCore.QRect(290, 160, 221, 16))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.widget)
        self.label_38.setGeometry(QtCore.QRect(310, 190, 261, 16))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.widget)
        self.label_39.setGeometry(QtCore.QRect(280, 220, 291, 16))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.widget)
        self.label_40.setGeometry(QtCore.QRect(290, 250, 261, 16))
        self.label_40.setObjectName("label_40")
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "电影名称："))
        self.label_2.setText(_translate("Dialog", "导演："))
        self.label_3.setText(_translate("Dialog", "演员:"))
        self.label_4.setText(_translate("Dialog", "类型:"))
        self.label_9.setText(_translate("Dialog", "国家:"))
        self.label_10.setText(_translate("Dialog", "语言:"))
        self.label_11.setText(_translate("Dialog", "上映时间:"))
        self.label_12.setText(_translate("Dialog", "时长:"))
        self.label_13.setText(_translate("Dialog", "imdb:"))
        self.label_14.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">简介：</span></p></body></html>"))
        self.label_15.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#000000;\">评分:</span><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#ff0000;\">9.4</span></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "简介内容"))
        self.label_17.setText(_translate("Dialog", "TextLabel"))
        self.label_18.setText(_translate("Dialog", "TextLabel"))
        self.label_19.setText(_translate("Dialog", "TextLabel"))
        self.label_35.setText(_translate("Dialog", "TextLabel"))
        self.label_36.setText(_translate("Dialog", "TextLabel"))
        self.label_37.setText(_translate("Dialog", "TextLabel"))
        self.label_38.setText(_translate("Dialog", "TextLabel"))
        self.label_39.setText(_translate("Dialog", "TextLabel"))
        self.label_40.setText(_translate("Dialog", "TextLabel"))

        self.funlist = [
            self.label_17.setText,
            self.label_18.setText,
            self.label_19.setText,
            self.label_35.setText,
            self.label_36.setText,
            self.label_37.setText,
            self.label_38.setText,
            self.label_39.setText,
            self.label_40.setText,
            self.label_16.setText,
            self.label_15.setText
        ]

    def set_value(self, id, mydb):

        cursor = mydb.cursor()
        cursor.execute('select * from spiders.movies where id = ' + str(id))
        result = list(cursor.fetchall()[0])
        result[
            -1] = '<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#000000;\">评分:</span><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#ff0000;\">' + \
                  result[-1] + '</span></p></body></html>'
        result.pop(0)
        for i in range(len(self.funlist)):
            self.funlist[i](result[i])

        cursor.execute(f"select name from spiders.movies where id = {id}")
        image_name = cursor.fetchall()[0][0]
        print(image_name)
        image_name_path = f'C:/Users/xiaoqi/Documents/Python_Spider_mysql/images/{image_name}'
        jpg = QtGui.QPixmap(image_name_path).scaled(self.jpg_label.width(), self.jpg_label.height())
        self.jpg_label.setPixmap(jpg)



    def showContextMenu(self, event):
        global x, y
        self.setContextMenuPolicy(self.contextMenuPolicy())
        self.customContextMenuRequested.connect(self.showContextMenu)

        # 创建QMenu
        self.contextMenu = QMenu(self)
        self.actionA = self.contextMenu.addAction(QIcon("dio.jpg"), u'|  动作A')
        self.actionB = self.contextMenu.addAction(QIcon("dio.jpg"), u'|  动作B')
        self.actionC = self.contextMenu.addAction(QIcon("dio.jpg"), u'|  动作C')
        print(x, y)
        self.contextMenu.move(1250, 479)
        self.contextMenu.show()

    def mouseMoveEvent(self, event):
        global x, y
        s = event.globalPos()
        self.setMouseTracking(True)
        print(x,y)
        x = s.x()
        y = s.y()

