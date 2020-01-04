import os
import sys

from PyQt5.QtGui import QImage, QPixmap
from ui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot


class Button(QPushButton):
    def __init__(self):
        super().__init__()
        self.button = ui.b1
        self.label1 = ui.label_l
        self.button_top = ui.b2
        self.label2 = ui.label_r
        self.lb_up = ui.lb_up
        self.lb_down = ui.lb_down
        self.rb_up = ui.rb_up
        self.rb_down = ui.rb_down
        self.llb_up = ui.llb_up
        self.rrb_down = ui.rrb_down
        self.hand_to = ui.hand_to
        self.auto_to = ui.auto_to
        self.path_back = ui.path_back
        self.path_top = ui.path_top
        self.button.clicked.connect(self.show_image)
        self.button_top.clicked.connect(self.show_image2)
        self.lb_up.clicked.connect(self.back_image1)
        self.rb_up.clicked.connect(self.back_image2)
        self.llb_up.clicked.connect(self.back_image3)
        self.lb_down.clicked.connect(self.next_image1)
        self.rb_down.clicked.connect(self.next_image2)
        self.rrb_down.clicked.connect(self.next_image3)
        self.hand_to.clicked.connect(self.hand_to_image)
        self.auto_to.clicked.connect(self.auto_to_image)
    def show_image(self):
        try:
            self.dir_path = QtWidgets.QFileDialog.getExistingDirectory(self, '选择背景文件夹')
            file = str(self.dir_path)
            if file != '':
                self.path_back.setText(file)
            dir_list = os.listdir(self.dir_path)
            img_list = []
            for dir in dir_list:
                suffix_list = ['jpg', 'png', 'jpeg', 'bmp']
                if dir.split('.')[-1].lower() in suffix_list:
                    img_list.append(dir)
            if len(img_list) > 0:
                #图像索引字典
                self.img_index_dict = dict()
                for i, d in enumerate(img_list):
                    self.img_index_dict[i] = d
                self.current_index = 0
        #         当前图片文件路径
                self.current_filename = os.path.join(self.dir_path, self.img_index_dict[self.current_index])
        #         实例化一个图像
                self.image = QtGui.QImage(self.current_filename)
                
                pixImg = QtGui.QPixmap.fromImage(self.image.scaled(self.label1.size()))
                self.label1.setPixmap(pixImg)
            else:
                QtWidgets.QMessageBox.information(self, '提示', '文件夹没有发现图片文件！', QtWidgets.QMessageBox.Ok)
        except Exception as e:
            print(repr(e))
    def show_image2(self):
        try:
            self.dir_path = QtWidgets.QFileDialog.getExistingDirectory(self, '选择背景文件夹')
            file = str(self.dir_path)
            if file != '':
                self.path_back.setText(file)
            dir_list = os.listdir(self.dir_path)
            img_list = []
            for dir in dir_list:
                suffix_list = ['jpg', 'png', 'jpeg', 'bmp']
                if dir.split('.')[-1].lower() in suffix_list:
                    img_list.append(dir)
            if len(img_list) > 0:
                #图像索引字典
                self.img_index_dict = dict()
                for i, d in enumerate(img_list):
                    self.img_index_dict[i] = d
                self.current_index = 0
        #         当前图片文件路径
                self.current_filename = os.path.join(self.dir_path, self.img_index_dict[self.current_index])
        #         实例化一个图像
                self.image = QtGui.QImage(self.current_filename)
                pixImg = QtGui.QPixmap.fromImage(self.image.scaled(self.label2.size()))
                self.label2.setPixmap(pixImg)
            else:
                QtWidgets.QMessageBox.information(self, '提示', '文件夹没有发现图片文件！', QtWidgets.QMessageBox.Ok)
        except Exception as e:
            print(repr(e))
    def next_image1(self):
        self.current_index += 1
        if self.current_index in self.img_index_dict.keys():
            self.current_filename = os.path.join(self.dir_path, self.img_index_dict[self.current_index])
            self.image = QtGui.QImage(self.current_filename)
            pixImg = QtGui.QPixmap.fromImage(self.image.scaled(self.label1.size()))
            self.label1.setPixmap(pixImg)
        else:
            self.current_index -= 1
            QtWidgets.QMessageBox.information(self, '提示', '所有图片已标注完！', QtWidgets.QMessageBox.Ok)
    def next_image2(self):
        self.current_index += 1
        if self.current_index in self.img_index_dict.keys():
            self.current_filename = os.path.join(self.dir_path, self.img_index_dict[self.current_index])
            self.image = QtGui.QImage(self.current_filename)
            pixImg = QtGui.QPixmap.fromImage(self.image.scaled(self.label2.size()))
            self.label2.setPixmap(pixImg)
        else:
            self.current_index -= 1
            QtWidgets.QMessageBox.information(self, '提示', '所有图片已标注完！', QtWidgets.QMessageBox.Ok)
    def next_image3(self):
        self.current_index += 1
        if self.current_index in self.img_index_dict.keys():
            self.current_filename = os.path.join(self.dir_path, self.img_index_dict[self.current_index])
            self.image = QtGui.QImage(self.current_filename)
            pixImg = QtGui.QPixmap.fromImage(self.image.scaled(self.label3.size()))
            self.label3.setPixmap(pixImg)
        else:
            self.current_index -= 1
            QtWidgets.QMessageBox.information(self, '提示', '所有图片已标注完！', QtWidgets.QMessageBox.Ok)
    def back_image1(self):
        self.current_index -= 1
        if self.current_index in self.img_index_dict.keys():
            self.current_filename = os.path.join(self.dir_path, self.img_index_dict[self.current_index])
            self.image = QtGui.QImage(self.current_filename)
            pixImg = QtGui.QPixmap.fromImage(self.image.scaled(self.label1.size()))
            self.label1.setPixmap(pixImg)
        else:
            self.current_index += 1
            QtWidgets.QMessageBox.information(self, '提示', '所有图片已标注完！', QtWidgets.QMessageBox.Ok)
    def back_image2(self):
        self.current_index -= 1
        if self.current_index in self.img_index_dict.keys():
            self.current_filename = os.path.join(self.dir_path, self.img_index_dict[self.current_index])
            self.image = QtGui.QImage(self.current_filename)
            pixImg = QtGui.QPixmap.fromImage(self.image.scaled(self.label2.size()))
            self.label2.setPixmap(pixImg)
        else:
            self.current_index += 1
            QtWidgets.QMessageBox.information(self, '提示', '所有图片已标注完！', QtWidgets.QMessageBox.Ok)
    def back_image3(self):
        self.current_index -= 1
        if self.current_index in self.img_index_dict.keys():
            self.current_filename = os.path.join(self.dir_path, self.img_index_dict[self.current_index])
            self.image = QtGui.QImage(self.current_filename)
            pixImg = QtGui.QPixmap.fromImage(self.image.scaled(self.label3.size()))
            self.label3.setPixmap(pixImg)
        else:
            self.current_index += 1
            QtWidgets.QMessageBox.information(self, '提示', '所有图片已标注完！', QtWidgets.QMessageBox.Ok)
    def hand_to_image(self):
        print("手动生成图片")
    def auto_to_image(self):
        print("演化生成图片")
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    bb = Button()
    sys.exit(app.exec_())
