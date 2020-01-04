from PyQt5 import QtWidgets, QtCore, QtGui
import sys,os
import traceback
from PIL import Image
import random

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图片合成") # 窗口标题
        self.setFixedSize(1000,800) # 设置窗口宽和高
        # 主控件和主控件布局
        self.main_widget = QtWidgets.QWidget() # 窗口主控件
        self.main_layout = QtWidgets.QGridLayout() # 窗口主控件布局
        self.main_widget.setLayout(self.main_layout)

        # 背景图像展示控件
        self.img_widget = QtWidgets.QWidget()
        self.img_layout = QtWidgets.QHBoxLayout()
        self.img_widget.setLayout(self.img_layout)
        # 背景图像视图标签占位
        self.img_view = QtWidgets.QLabel("背景图片显示！")
        self.img_view.setAlignment(QtCore.Qt.AlignCenter)
        self.img_view.setFixedSize(400,400)
        self.img_layout.addWidget(self.img_view)

        # 前景图像展示控件1
        self.img_widget1 = QtWidgets.QWidget()
        self.img_layout1 = QtWidgets.QHBoxLayout()
        self.img_widget1.setLayout(self.img_layout1)
        # 前景图像视图标签占位1
        self.img_view1 = QtWidgets.QLabel("前景图片显示！")
        self.img_view1.setAlignment(QtCore.Qt.AlignCenter)
        self.img_view1.setFixedSize(400, 400)
        self.img_layout1.addWidget(self.img_view1)

        # 合成图像展示控件2
        self.img_widget2 = QtWidgets.QWidget()
        self.img_layout2 = QtWidgets.QHBoxLayout()
        self.img_widget2.setLayout(self.img_layout2)
        # 合成图像视图标签占位2
        self.img_view2 = QtWidgets.QLabel("合成图片显示！")
        self.img_view2.setAlignment(QtCore.Qt.AlignCenter)
        self.img_view2.setFixedSize(400, 400)
        self.img_layout2.addWidget(self.img_view2)

        # 按钮
        #选择背景文件夹
        self.folder_input = QtWidgets.QLineEdit()
        self.folder_input.setReadOnly(True)
        self.folder_btn = QtWidgets.QPushButton("选择背景文件夹")
        #self.folder_btn.clicked.connect(self.select_folder)
        self.folder_btn.clicked.connect(self.select_img_click)
        #选择前景文件夹
        self.wm_input = QtWidgets.QLineEdit()
        self.wm_input.setReadOnly(True)
        self.wm_btn = QtWidgets.QPushButton("选择前景文件夹")
        #self.wm_btn.clicked.connect(self.select_wm_img)
        self.wm_btn.clicked.connect(self.select_img_click1)
        #保存目录
        self.save_input = QtWidgets.QLineEdit()
        self.save_input.setReadOnly(True)
        self.save_btn = QtWidgets.QPushButton("保存目录")
        self.save_btn.clicked.connect(self.select_save_folder)
        #生成位置
        self.position_label = QtWidgets.QLabel('生成位置：')
        self.position_box = QtWidgets.QComboBox()
        self.position_box.addItem("左上")
        self.position_box.addItem("左下")
        self.position_box.addItem("右上")
        self.position_box.addItem("右下")
        self.position_box.addItem("居中")
        self.position_box.addItem("随机")

        #背景图片上一张和下一张
        self.previous_img_btn = QtWidgets.QPushButton("上一张")
        self.previous_img_btn.setEnabled(False)
        self.previous_img_btn.clicked.connect(self.previous_img_click)
        self.next_img_btn = QtWidgets.QPushButton("下一张")
        self.next_img_btn.setEnabled(False)
        self.next_img_btn.clicked.connect(self.next_img_click)

        #前景图片上一张和下一张
        self.previous_img_btn1 = QtWidgets.QPushButton("上一张")
        self.previous_img_btn1.setEnabled(False)
        self.previous_img_btn1.clicked.connect(self.previous_img_click1)
        self.next_img_btn1 = QtWidgets.QPushButton("下一张")
        self.next_img_btn1.setEnabled(False)
        self.next_img_btn1.clicked.connect(self.next_img_click1)

        # 合成图片上一张和下一张
        self.previous_img_btn2 = QtWidgets.QPushButton("上一张")
        self.previous_img_btn2.setEnabled(False)
        self.previous_img_btn2.clicked.connect(self.previous_img_click2)
        self.next_img_btn2 = QtWidgets.QPushButton("下一张")
        self.next_img_btn2.setEnabled(False)
        self.next_img_btn2.clicked.connect(self.next_img_click2)

        #生成图片
        self.submit_btn = QtWidgets.QPushButton("手动生成")
        self.submit_btn.clicked.connect(self.generate_img)
        self.submit_btn1 = QtWidgets.QPushButton("演化生成")
        #按钮放到布局
        self.main_layout.addWidget(self.folder_input,0, 0, 1, 2)
        self.main_layout.addWidget(self.folder_btn, 0, 2, 1, 1)
        self.main_layout.addWidget(self.wm_input, 1, 0, 1, 2)
        self.main_layout.addWidget(self.wm_btn, 1, 2, 1, 1)
        self.main_layout.addWidget(self.img_widget, 2, 0, 1, 1)  # 起始行，起始列，占用行，占用列
        self.main_layout.addWidget(self.img_widget1, 2, 1, 1, 1)
        self.main_layout.addWidget(self.previous_img_btn,3, 0 ,1, 1)
        self.main_layout.addWidget(self.next_img_btn, 4, 0, 1, 1)
        self.main_layout.addWidget(self.previous_img_btn1, 3, 1, 1, 1)
        self.main_layout.addWidget(self.next_img_btn1, 4, 1, 1, 1)
        self.main_layout.addWidget(self.img_widget2, 5, 0, 1, 2)
        self.main_layout.addWidget(self.previous_img_btn2, 6, 0, 1, 1)
        self.main_layout.addWidget(self.next_img_btn2, 6, 1, 1, 1)
        self.main_layout.addWidget(self.submit_btn, 7, 0, 1, 1)
        self.main_layout.addWidget(self.submit_btn1, 7, 1, 1, 1)
        self.main_layout.addWidget(self.position_box, 7, 2, 1, 1)
        self.main_layout.addWidget(self.save_input, 8, 0, 1, 2)
        self.main_layout.addWidget(self.save_btn, 8, 2, 1, 1)
        self.setCentralWidget(self.main_widget) # 设置窗口初始化控件


    # 选择背景目录按钮
    def select_img_click(self):
        try:
            self.dir_path = QtWidgets.QFileDialog.getExistingDirectory(self,'选择背景文件夹')
            # print(self.dir_path)
            file = str(self.dir_path)
            print('文件夹为：', file)
            if file != '':
                self.folder_input.setText(file)
            dir_list = os.listdir(self.dir_path)
            img_list = []
            for dir in dir_list:
                suffix_list = ['jpg','png','jpeg','bmp',]
                if dir.split('.')[-1].lower() in suffix_list:
                    # print(dir)
                    img_list.append(dir)
            if len(img_list) > 0:
                # 图像文件索引字典
                self.img_index_dict = dict()
                for i,d in enumerate(img_list):
                    self.img_index_dict[i] = d
                # print(self.img_index_dict)
                self.current_index = 0 # 当前的图像索引
                # 当前图片文件路径
                self.current_filename = os.path.join(
                    self.dir_path,self.img_index_dict[self.current_index]
                )
                # 实例化一个图像
                image = QtGui.QImage(self.current_filename)
                self.img_width = image.width()  # 图片宽度
                self.img_height = image.height()  # 图片高度
                self.img_scale = 1
                self.image = image.scaled(self.img_width * self.img_scale, self.img_height * self.img_scale)
                # 在img_view控件中显示图像
                self.img_view.setPixmap(QtGui.QPixmap.fromImage(self.image))
                # 启用其他按钮
                self.previous_img_btn.setEnabled(True)
                self.next_img_btn.setEnabled(True)
            else:
                QtWidgets.QMessageBox.information(
                    self,'提示','文件夹没有发现图片文件！',
                    QtWidgets.QMessageBox.Ok
                )
        except Exception as e:
            print(repr(e))

    # 选择前景目录按钮1
    def select_img_click1(self):
        try:
            self.dir_path1 = QtWidgets.QFileDialog.getExistingDirectory(self, '选择前景文件夹')
            # print(self.dir_path)
            # file1 = str(self.dir_path1)
            # print('文件夹为：', file1)
            # if file1 != '':
            #     self.wm_input.setText(file1)
            imgName, imgType = QtWidgets.QFileDialog.getOpenFileName(self, "选择水印图片", "", "*.jpg;;*.png;;All Files(*)")
            jpg = QtGui.QPixmap(imgName).scaled(self.img_view1.width(), self.img_view1.height())
            self.img_view1.setPixmap(jpg)
            jpg1 = str(imgName)
            print("水印图片为：", jpg1)
            if jpg != '':
                self.wm_input.setText(jpg1)
            dir_list1 = os.listdir(self.dir_path1)
            img_list1 = []
            for dir in dir_list1:
                suffix_list1 = ['jpg', 'png', 'jpeg', 'bmp', ]
                if dir.split('.')[-1].lower() in suffix_list1:
                    # print(dir)
                    img_list1.append(dir)
            if len(img_list1) > 0:
                # 图像文件索引字典
                self.img_index_dict1 = dict()
                for i, d in enumerate(img_list1):
                    self.img_index_dict1[i] = d
                # print(self.img_index_dict)
                self.current_index1 = 0  # 当前的图像索引
                # 当前图片文件路径
                self.current_filename1 = os.path.join(
                    self.dir_path1, self.img_index_dict1[self.current_index1]
                )
                # 实例化一个图像
                image1 = QtGui.QImage(self.current_filename1)
                self.img_width1 = image1.width()  # 图片宽度
                self.img_height1 = image1.height()  # 图片高度
                self.img_scale1 = 1
                self.image1 = image1.scaled(self.img_width1 * self.img_scale1, self.img_height1 * self.img_scale1)

                # 在img_view控件中显示图像
                self.img_view1.setPixmap(QtGui.QPixmap.fromImage(self.image1))

                # 启用其他按钮
                self.previous_img_btn1.setEnabled(True)
                self.next_img_btn1.setEnabled(True)
            else:
                QtWidgets.QMessageBox.information(
                    self, '提示', '文件夹没有发现图片文件！',
                    QtWidgets.QMessageBox.Ok
                )
        except Exception as e:
            print(repr(e))

    # 背景下一张图片
    def next_img_click(self):
        # 当前图像索引加1
        self.current_index += 1
        if self.current_index in self.img_index_dict.keys():
            # 当前图片文件路径
            self.current_filename = os.path.join(
                self.dir_path, self.img_index_dict[self.current_index]
            )
            # 实例化一个图像
            image = QtGui.QImage(self.current_filename)
            self.img_width = image.width()  # 图片宽度
            self.img_height = image.height()  # 图片高度
            self.img_scale = 1
            self.image = image.scaled(self.img_width * self.img_scale, self.img_height * self.img_scale)
            # 在img_view控件中显示图像
            self.img_view.setPixmap(QtGui.QPixmap.fromImage(self.image))
        else:
            self.current_index -= 1
            QtWidgets.QMessageBox.information(
                self, '提示', '所有图片已标注完！',
                QtWidgets.QMessageBox.Ok
            )

    # 前景下一张图片
    def next_img_click1(self):
        # 当前图像索引加1
        self.current_index1 += 1
        if self.current_index1 in self.img_index_dict1.keys():
            # 当前图片文件路径
            self.current_filename1 = os.path.join(
                self.dir_path1, self.img_index_dict1[self.current_index1]
            )
            # 实例化一个图像
            image1 = QtGui.QImage(self.current_filename1)
            self.img_width1 = image1.width()  # 图片宽度
            self.img_height1 = image1.height()  # 图片高度
            self.img_scale1 = 1
            self.image1 = image1.scaled(self.img_width1 * self.img_scale1, self.img_height1 * self.img_scale1)
            # 在img_view控件中显示图像
            self.img_view1.setPixmap(QtGui.QPixmap.fromImage(self.image1))
        else:
            self.current_index1 -= 1
            QtWidgets.QMessageBox.information(
                self, '提示', '所有图片已标注完！',
                QtWidgets.QMessageBox.Ok
            )

    # 合成下一张图片
    def next_img_click2(self):
        # 当前图像索引加1
        self.current_index2 += 1
        if self.current_index2 in self.img_index_dict2.keys():
            # 当前图片文件路径
            self.current_filename2 = os.path.join(
                self.dir_path2, self.img_index_dict2[self.current_index1]
            )
            # 实例化一个图像
            image2 = QtGui.QImage(self.current_filename2)
            self.img_width2 = image2.width()  # 图片宽度
            self.img_height2 = image2.height()  # 图片高度
            self.img_scale2 = 1
            self.image2 = image2.scaled(self.img_width2 * self.img_scale2, self.img_height2 * self.img_scale2)
            # 在img_view控件中显示图像
            self.img_view2.setPixmap(QtGui.QPixmap.fromImage(self.image2))
        else:
            self.current_index2 -= 1
            QtWidgets.QMessageBox.information(
                self, '提示', '所有图片已标注完！',
                QtWidgets.QMessageBox.Ok
            )

    # 背景上一张图片
    def previous_img_click(self):
        # 当前图像索引加1
        self.current_index -= 1
        if self.current_index in self.img_index_dict.keys():
            # 当前图片文件路径
            self.current_filename = os.path.join(
                self.dir_path, self.img_index_dict[self.current_index]
            )
            # 实例化一个图像
            image = QtGui.QImage(self.current_filename)
            self.img_width = image.width()  # 图片宽度
            self.img_height = image.height()  # 图片高度
            self.img_scale = 1
            self.image = image.scaled(self.img_width * self.img_scale, self.img_height * self.img_scale)

            # 在img_view控件中显示图像
            self.img_view.setPixmap(QtGui.QPixmap.fromImage(self.image))
        else:
            self.current_index += 1
            QtWidgets.QMessageBox.information(
                self, '提示', '图片列表到顶了！',
                QtWidgets.QMessageBox.Ok
            )

    # 前景上一张图片
    def previous_img_click1(self):
        # 当前图像索引加1
        self.current_index1 -= 1
        if self.current_index1 in self.img_index_dict1.keys():
            # 当前图片文件路径
            self.current_filename1 = os.path.join(
                self.dir_path1, self.img_index_dict1[self.current_index1]
            )
            # 实例化一个图像
            image1 = QtGui.QImage(self.current_filename1)
            self.img_width1 = image1.width()  # 图片宽度
            self.img_height1 = image1.height()  # 图片高度
            self.img_scale1 = 1
            self.image1 = image1.scaled(self.img_width1 * self.img_scale1, self.img_height1 * self.img_scale1)
            # 在img_view控件中显示图像
            self.img_view1.setPixmap(QtGui.QPixmap.fromImage(self.image1))
        else:
            self.current_index1 += 1
            QtWidgets.QMessageBox.information(
                self, '提示', '图片列表到顶了！',
                QtWidgets.QMessageBox.Ok
            )

    # 合成上一张图片
    def previous_img_click2(self):
        # 当前图像索引加1
        self.current_index2 -= 1
        if self.current_index2 in self.img_index_dict2.keys():
            # 当前图片文件路径
            self.current_filename2 = os.path.join(
                self.dir_path2, self.img_index_dict2[self.current_index2]
            )
            # 实例化一个图像
            image2 = QtGui.QImage(self.current_filename2)
            self.img_width2 = image2.width()  # 图片宽度
            self.img_height2 = image2.height()  # 图片高度
            self.img_scale2 = 1
            self.image2 = image2.scaled(self.img_width2 * self.img_scale2, self.img_height2 * self.img_scale2)
            # 在img_view控件中显示图像
            self.img_view2.setPixmap(QtGui.QPixmap.fromImage(self.image2))
        else:
            self.current_index2 += 1
            QtWidgets.QMessageBox.information(
                self, '提示', '图片列表到顶了！',
                QtWidgets.QMessageBox.Ok
            )

    # 重写鼠标滚轮事件
    def wheelEvent(self, event):
        # 如果按住了Ctrl
        if event.modifiers() == QtCore.Qt.ControlModifier:
            try:
                delta = event.angleDelta().y()
                if delta > 0:
                    self.img_scale += 0.25
                    self.image_scaled = self.image.scaled(self.img_width * self.img_scale,self.img_height * self.img_scale)
                    self.img_view.setPixmap(QtGui.QPixmap.fromImage(self.image_scaled))
                    self.statusBar().showMessage("当前图片缩放比例为：{}%".format(self.img_scale * 100))
                elif delta < 0:
                    if self.img_scale > 0.25:
                       self.img_scale -= 0.25
                       self.image_scaled = self.image.scaled(self.img_width * self.img_scale,self.img_height * self.img_scale)
                       self.img_view.setPixmap(QtGui.QPixmap.fromImage(self.image_scaled))
                       self.statusBar().showMessage("当前图片缩放比例为：{}%".format(self.img_scale * 100))
            except Exception as e:
                print(traceback.print_exc())
                print(repr(e))

    # 选择图片文件夹
    def select_folder(self):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self, "选择文件夹"))
        print('文件夹为：', file)
        if file != '':
            self.folder_input.setText(file)

    # 选择水印图片
    def select_wm_img(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, '选择水印图片', '', 'Images (*.png *.xpm *.jpg)'
        )
        print("水印图片为：", file)
        if file != '':
            self.wm_input.setText(file)

    # 选择保存目录
    def select_save_folder(self):
        # file = str(QtWidgets.QFileDialog.getExistingDirectory(self, "保存目录"))
        # print('文件夹为：', file)
        # if file != '':
        #     self.save_input.setText(file)
        try:
            self.dir_path2 = QtWidgets.QFileDialog.getExistingDirectory(self,'保存目录')
            # print(self.dir_path)
            file2 = str(self.dir_path2)
            print('文件夹为：', file2)
            if file2 != '':
                self.save_input.setText(file2)
            dir_list2 = os.listdir(self.dir_path2)
            img_list2 = []
            for dir in dir_list2:
                suffix_list2 = ['jpg','png','jpeg','bmp',]
                if dir.split('.')[-1].lower() in suffix_list2:
                    # print(dir)
                    img_list2.append(dir)
            if len(img_list2) > 0:
                # 图像文件索引字典
                self.img_index_dict2 = dict()
                for i,d in enumerate(img_list2):
                    self.img_index_dict2[i] = d
                # print(self.img_index_dict)
                self.current_index2 = 0 # 当前的图像索引
                # 当前图片文件路径
                self.current_filename2 = os.path.join(
                    self.dir_path2,self.img_index_dict2[self.current_index2]
                )
                # 实例化一个图像
                image2 = QtGui.QImage(self.current_filename2)
                self.img_width2 = image2.width()  # 图片宽度
                self.img_height2 = image2.height()  # 图片高度
                self.img_scale2 = 0.5
                self.image2 = image2.scaled(self.img_width2 * self.img_scale2, self.img_height2 * self.img_scale2)
                # 在img_view控件中显示图像
                self.img_view2.setPixmap(QtGui.QPixmap.fromImage(self.image2))
                # 启用其他按钮
                self.previous_img_btn2.setEnabled(True)
                self.next_img_btn2.setEnabled(True)
            else:
                QtWidgets.QMessageBox.information(
                    self,'提示','文件夹没有发现图片文件！',
                    QtWidgets.QMessageBox.Ok
                )
        except Exception as e:
            print(repr(e))

    # 生成水印图片
    def generate_img(self):
        try:
            print("获取图片目录及水印文件名")
            folder_text = self.folder_input.text()
            wm_text = self.wm_input.text()
            save_text = self.save_input.text()
            position_text = self.position_box.currentText()
            print('判断是否为空')
            if folder_text != '' and wm_text != '':
                self.submit_btn.setEnabled(False)
                self.genare_thread = WmThread(
                    wm_file=wm_text,
                    fpath=folder_text,
                    save_path=save_text,
                    position=position_text
                )
                print('启动线程')
                self.genare_thread.finished_signal.connect(self.thread_resp)
                self.genare_thread.start()

        except Exception as e:
            print(traceback.print_exc())

    def thread_resp(self, value):
        if value == 1:
            QtWidgets.QMessageBox.information(self, '提示', '处理完成！', QtWidgets.QMessageBox.Yes)
        if value == 0:
            QtWidgets.QMessageBox.information(self, '提示', '处理出错！', QtWidgets.QMessageBox.Yes)
        self.submit_btn.setEnabled(True)

class WmThread(QtCore.QThread):
    finished_signal = QtCore.pyqtSignal(int) # 使用PySide2模块需要将pyqtSignal改成Signal

    def __init__(self,parent=None,wm_file=None,fpath=None,save_path=None,position=None):
        super().__init__(parent)
        self.wm_file = wm_file
        self.fpath = fpath
        self.save_path = save_path
        self.position = position
        print(self.wm_file,self.fpath)

    # 获取文件夹图片
    def get_folder(self,fpath):
        try:
            img_suffix_list = ['png', 'jpg', 'bmp']
            for i in os.listdir(fpath):
                if i.split('.')[-1] in img_suffix_list:
                    img_path = fpath + '/' + i
                    self.img_water_mark(img_file=img_path,wm_file=self.wm_file)
        except Exception as e:
            print(traceback.print_exc())

    # 图片添加水印
    def img_water_mark(self,img_file, wm_file):
        try:
            img = Image.open(img_file)  # 打开图片
            watermark = Image.open(wm_file)  # 打开水印
            img_size = img.size
            wm_size = watermark.size
            # 如果图片大小小于水印大小
            if img_size[0] < wm_size[0]:
                watermark.resize(tuple(map(lambda x: int(x * 0.5), watermark.size)))
            print('图片大小：', img_size,"水印位置：",self.position)
            if self.position == '左上':
                wm_position = (0,0)
            elif self.position == '左下':
                wm_position = (0,img_size[1]-wm_size[1])
            elif self.position == '右上':
                wm_position = (img_size[0]-wm_size[0],0)
            elif self.position == '右下':
                wm_position = (img_size[0]-wm_size[0],img_size[1]-wm_size[1])
            elif self.position == '居中':
                wm_position = (img_size[0]//2-wm_size[0]//2,img_size[1]//2-wm_size[1]//2)
            elif self.position == '随机':
                wm_position = (random.randrange(0,img_size[0]),random.randrange(0,img_size[1]))
            layer = Image.new('RGBA', img.size)  # 新建一个图层
            layer.paste(watermark, wm_position)  # 将水印图片添加到图层上
            mark_img = Image.composite(layer, img, layer)
            new_file_name = '/new_'+img_file.split('/')[-1]
            if self.save_path == '':
                mark_img.save(self.fpath+new_file_name)
            else:
                mark_img.save(self.save_path + new_file_name)
        except Exception as e:
            print(traceback.print_exc())

    def run(self):
        try:
            print("开始处理……")
            self.get_folder(fpath=self.fpath)
            self.finished_signal.emit(1)
        except Exception as e:
            print(traceback.print_exc())
            self.finished_signal.emit(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = MainApp()
    my.show()
    sys.exit(app.exec_())
