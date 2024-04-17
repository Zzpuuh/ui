from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 575)
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 170, 731, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(300, 70, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 450, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 450, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 450, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 450, 75, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(670, 450, 75, 24))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "书名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "作者"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "存放位置"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "原价"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "出版年份"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "出版社"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "数量"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "价格"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "备注"))
        self.label.setText(_translate("Form", "书籍管理系统"))
        self.pushButton.setText(_translate("Form", "添加"))
        self.pushButton_2.setText(_translate("Form", "删除"))
        self.pushButton_3.setText(_translate("Form", "查询"))
        self.pushButton_4.setText(_translate("Form", "更新"))
        self.pushButton_5.setText(_translate("Form", "退出"))

import sqlite3

class database:
    def __init__(self,db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        # 书名,作者, 存放位置, 原价, 出版年份, 出版社, 数量, 购买日期, 购买价格, 备注
        create_table = '''create table if not exists
                            books(book_name primary key,book_author, book_pos,price, year,
                            pub, nums,day,buy_price,ps)        
        
        
        '''
        self.con.execute(create_table)

    def close(self):
        self.cur.close()
        self.con.close()

    def add(self,x):
        #添加一条记录
        add_string = '''insert into books(book_name,book_author, book_pos,price, year,
                            pub, nums,day,buy_price,ps) values (?,?,?,?,?,?,?,?,?,?)

                    '''
        self.cur.execute(add_string,x)
        self.con.commit() #确认记录的写入
    
    def show_all(self):
        data_list = []
        self.cur.execute("select * from books")
        for item in self.cur:
            data_list.append(list(item))
        return data_list
    
    def delete(self,v):
        delete_string = 'DELETE FROM books WHERE book_name = '+'"'+v+'"'
        self.cur.execute(delete_string)
        self.con.commit() #确认记录的写入

    def find_data(self, name):  
        find_string = '''SELECT *  
                        FROM books  
                        WHERE book_name LIKE ?  
                        OR book_author LIKE ?  
                        OR book_pos LIKE ?
                        OR price LIKE ?
                        OR year LIKE ?
                        OR ps LIKE ?'''   
        params = ("%{}%".format(name), "%{}%".format(name), "%{}%".format(name),"%{}%".format(name), "%{}%".format(name), "%{}%".format(name))  
        self.cur.execute(find_string, params)  
        return self.cur.fetchall()
    
    def judge_name(self,n):
        # print(n)
        judge_string = 'SELECT COUNT(*) FROM books WHERE book_name = '+'"'+n+'"'

        self.cur.execute(judge_string)
        return self.cur.fetchall()[0][0]
    
    def updata(self,book):
        update_string = '''UPDATE books SET book_author=?, book_pos=?, price=?, year=?,  
                            pub=?, nums=?, day=?, buy_price=?, ps=? WHERE book_name=?  '''  
        params = book[1:]+[book[0]]
        self.cur.execute(update_string,params)  
        self.con.commit() #确认记录的写入

        






if __name__ =='__main__':
    # 书名,作者, 存放位置, 原价, 出版年份, 出版社, 数量, 购买日期, 购买价格, 备注

    db = database("books.db")
    x = ['高等数学', '同济大学数学组', '教材', '36.90', '1999', '同济大学出版社', '3', '2023-9-5', '25.00', '经典数学书']
    db.add(x)

    x = ['大学英语', '外国语组', '教材', '72.80', '2005', '清华大学出版社', '1', '2023-9-5', '52.00', '英语教材']
    db.add(x)

    x = ['小王子', '安托万·德·圣·埃克苏佩里', '小说', '23.6', '2015', '译文出版社', '1', '2020-1-2', '20.00', '经典小说']
    db.add(x)
    x = ['病隙碎笔', '史铁生', '散文', '25', '2008', '人民文学出版社', '1', '2021-11-6', '20.00', '对人生的诘问、探索与解答']
    db.add(x)    
    data = db.show_all()
    print(data)