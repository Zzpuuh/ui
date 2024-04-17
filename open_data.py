import sys
import sqlite3
from PyQt6.QtWidgets import (

       QMainWindow, QApplication, QDialog, QMessageBox,

       QFileDialog,QTableWidgetItem) #列出的项目除了QApplication，其余可根据界面增删

from PyQt6.QtGui import QImage, QPixmap

from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui, QtWidgets
from Ui_book import Ui_Form,database
from Ui_find import ui_find
from Ui_tianjia import Ui_add

from Ui_untitled import Ui_Dialog
from Ui_zhuce import Ui_reg

from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QSize

from PyQt6.QtMultimedia import QMediaPlayer 
from PyQt6.QtCore import QUrl 

class LogWindow(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,500)
        self.initBg()
        self.setupUi(self)
        self.label.setStyleSheet("QLabel { color: white; }")
        self.open() 
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_3.clicked.connect(self.find)
        self.pushButton_4.clicked.connect(self.updata)
        self.pushButton_5.clicked.connect(self.quit)

    def initBg(self):
        background = QLabel(self)
        background.setGeometry(self.rect())
        movie = QMovie("1.gif")
        movie.setScaledSize(QSize(800,500))
        background.setMovie(movie)
        movie.start()

        
    def quit(self):
        reply = QMessageBox.question(self, "确认", "确认退出?")
        if reply == QMessageBox.StandardButton.Yes:
            app = QApplication.instance()
            app.quit()

    def open(self):  
        title = "书名,作者,存放位置,原价,出版年份,出版社,数量,购买日期,购买价格,备注"  
        self.tableWidget.setColumnCount(len(title.split(',')))  
        self.tableWidget.setHorizontalHeaderLabels(title.split(','))  
 
        self.tableWidget.setRowCount(0)  
          
        db = database("books.db")  
        data = db.show_all()  
          
        for i, item in enumerate(data):    
            if i >= self.tableWidget.rowCount():  
                self.tableWidget.insertRow(self.tableWidget.rowCount())  
              
            for j, row in enumerate(item):  
                new_cell = QTableWidgetItem(str(row))  
                new_cell.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  
                self.tableWidget.setItem(i, j, new_cell)  
          
        self.tableWidget.resizeRowsToContents()  
        self.tableWidget.resizeColumnsToContents()

    def add(self):
        global add_win
        add_win = addWindow(self)
        add_win.show()


    def find(self):
        global find_win
        find_win = findWindow()
        book_win.hide()
        find_win.show()

    def updata(self):
        row = self.tableWidget.currentRow()
        # print(row)
        if self.tableWidget.item(row,0) == None:
            reply = QMessageBox.warning(self, "确认", "当前行没内容")
            if reply == QMessageBox.StandardButton.Yes:
                app = QApplication.instance()
                app.quit()
        else: 
            data_tableWidge = []
            for column in range(self.tableWidget.columnCount()):  
                item = self.tableWidget.item(row, column)  
                if item is not None:  
                    data_tableWidge.append(item.text())  
                else:  
                    data_tableWidge.append("") 
            global updata_win
            updata_win = updata_Window(data_tableWidge,self)
            updata_win.setWindowTitle("更新书籍")
            updata_win.show()

    def delete(self):
        reply = QMessageBox.question(self, "确认", "即将删除。是否继续？",  
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)  
        if reply == QMessageBox.StandardButton.Yes:
            row = self.tableWidget.currentRow()
            # print(row)
            if self.tableWidget.item(row,0) == None:
                reply = QMessageBox.warning(self, "确认", "当前行没内容")
                if reply == QMessageBox.StandardButton.Yes:
                    app = QApplication.instance()
                    app.quit()
            else:
                book_name = self.tableWidget.item(row,0).text()
                # print(book_name)
                self.tableWidget.removeRow(row)
                db = database("books.db")
                db.delete(book_name)
                # print(db.show_all())
        else:
            pass



class findWindow(QDialog, ui_find):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.find)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.clean)

    def back(self):
        find_win.hide()
        book_win.show()
    
    def find(self):
        self.textEdit_2.setText("") 
        find_name = self.textEdit.toPlainText()
        db = database("books.db")

        find_data = db.find_data(find_name)

        if find_data == []:
            reply = QMessageBox.warning(self, "确认", "没有搜索到对应的书籍")
            if reply == QMessageBox.StandardButton.Yes:
                app = QApplication.instance()
                app.quit()
            
        for row in find_data:  
            row_text = " ".join(item for item in row)  
            self.textEdit_2.append(row_text)  

    def clean(self):
        self.textEdit_2.setText("") 

        

class addWindow(QDialog, Ui_add):
    def __init__(self,log_win): 
        super().__init__() 
        self.setupUi(self)
        self.log_win = log_win
        self.pushButton.clicked.connect(self.ensure)
        self.pushButton_2.clicked.connect(self.clean)
        self.textEdit_list = [self.textEdit,self.textEdit_1,self.textEdit_2,self.textEdit_3,self.textEdit_4,self.textEdit_5,self.textEdit_6,self.textEdit_7,self.textEdit_8,self.textEdit_9]

    def ensure(self):
        find_name = self.textEdit.toPlainText()
        db = database("books.db")
        # print(find_name)
        find_data = db.judge_name(find_name)
        # print(find_data)
        if find_data > 0:
            reply = QMessageBox.warning(self, "确认", "库中已经有该书")
            if reply == QMessageBox.StandardButton.Yes:
                app = QApplication.instance()
                app.quit()
        else:
            book = []
            for textEdit_text in self.textEdit_list:
                book.append(textEdit_text.toPlainText())
            db.add(book)
            # db.show_all()
            for textEdit_text in self.textEdit_list:
                textEdit_text.clear()
            row_count = self.log_win.tableWidget.rowCount()  
            self.log_win.tableWidget.insertRow(row_count)  
            for column, value in enumerate(book):  
                item = QTableWidgetItem(str(value))  
                self.log_win.tableWidget.setItem(row_count, column, item)



    
    def clean(sekf):
        add_win.hide()


class updata_Window(QDialog, Ui_add):
    def __init__(self,data,log_win):
        self.data = data  
        self.log_win = log_win
        super().__init__() 
        self.setupUi(self)
        self.textEdit_list = [self.textEdit,self.textEdit_1,self.textEdit_2,self.textEdit_3,self.textEdit_4,self.textEdit_5,self.textEdit_6,self.textEdit_7,self.textEdit_8,self.textEdit_9]
        self.open()
        self.pushButton.clicked.connect(self.ensure)
        self.pushButton_2.clicked.connect(self.clean)
        

    def clean(self):
        updata_win.hide()
    
    def open(self):
        for i,Edit in enumerate(self.textEdit_list):
            Edit.setText(self.data[i])

    def ensure(self):
        find_name = self.textEdit.toPlainText()
        db = database("books.db")
        # print(find_name)
        # print(find_data)
        book = []
        for textEdit_text in self.textEdit_list:
            book.append(textEdit_text.toPlainText())
        # print(book[1:]+[book[0]])
        db.updata(book)
        # print(book)
        if find_name != self.data[0]:
            self.log_win.tableWidget.setItem(0, 0,  QTableWidgetItem(find_name))
        for row in range(self.log_win.tableWidget.rowCount()):  
            if self.log_win.tableWidget.item(row, 0).text() == find_name:  
                for col, text in enumerate(book):  
                    new_cell = QTableWidgetItem(str(text))  
                    self.log_win.tableWidget.setItem(row, col, new_cell)  





class LoginWindow(QDialog, Ui_Dialog):

    def __init__(self):

        super().__init__()

        self.initBg()  

        self.setupUi(self)
        self.setFixedSize(620,364)
        
        self.pushButton.clicked.connect(self.quit)
        self.pushButton_2.clicked.connect(self.to_reg)
        self.pushButton_3.clicked.connect(self.judge_user)
        # self.player = QMediaPlayer()  
        # self.music()


    def quit(self):

        reply = QMessageBox.question(self, "确认", "确认退出?")

        if reply == QMessageBox.StandardButton.Yes:

            app = QApplication.instance()

            app.quit()
    def initBg(self):
        background = QLabel(self)
        background.setGeometry(self.rect())
        movie = QMovie("bg.gif")
        movie.setScaledSize(QSize(620,500))
        background.setMovie(movie)
        movie.start()

    # def music(self):
    #     music_file = 'yuan.ogg'  

    #     url = QUrl.fromLocalFile(music_file)  
  
 
    #     self.player.setSource(url)  

    #     self.player.play() 



    def to_reg(self):#转到注册界面
        login_win.hide()
        reg_win.show()

    def judge_user(self):  
        name_use = self.lineEdit.text()  
        password_use = self.lineEdit_2.text()  
        with open('user.txt', 'r') as f:  
            for line in f:  
                id, name, password = line.split()  
                name = name.strip()  
                password = password.strip()  
                dict_user[name] = password  
    
        if name_use.strip() in dict_user and dict_user[name_use.strip()] == password_use:  
            reply = QMessageBox.question(self, "确认", "密码正确，欢迎进入。是否继续？",  
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)  
            if reply == QMessageBox.StandardButton.Yes:

                login_win.hide()
                book_win.show()
        else:  
            QMessageBox.warning(self, "错误", "密码错误")
        self.lineEdit.clear()
        self.lineEdit_2.clear()


class zhuceWindow(QDialog, Ui_reg):

    def __init__(self):

        super().__init__()
        self.initBg()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.quit)
        self.pushButton_2.clicked.connect(self.zhuce)


    def zhuce(self):#将注册账号密码存回
        name_use = self.lineEdit.text()
        password_use = self.lineEdit_2.text()
        dict_user[name_use] = password_use
        reply = QMessageBox.warning(self, "确认", "注册成功")
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        if reply == QMessageBox.StandardButton.Yes:
            app = QApplication.instance()
            app.quit()
        # print(dict_user)
        
            

    def initBg(self):
        background = QLabel(self)
        background.setGeometry(self.rect())
        movie = QMovie("bg.gif")
        movie.setScaledSize(QSize(620,500))
        background.setMovie(movie)
        movie.start()


 
    def quit(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        reg_win.hide()
        login_win.show()



if __name__ == '__main__':
    dict_user = {}
    app = QApplication(sys.argv)
    book_win = LogWindow()
    book_win.setWindowTitle("书籍")
    login_win = LoginWindow()
    login_win.setWindowTitle("登录")
    reg_win = zhuceWindow()
    reg_win.setWindowTitle("注册")
    login_win.show()

    sys.exit(app.exec())
