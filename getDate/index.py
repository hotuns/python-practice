# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   getdate.py
@Time    :   2019/07/15 13:33:22
把文件夹内的所有文件名(还有文件内的字段),从时间戳格式修改成人类可读的格式

'''


from datetime import datetime
import os
import json
import re

from tkinter import *
import tkinter.filedialog


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.path = StringVar()
        self.info = StringVar()
        self.v = IntVar()
        self.createWidgets()
        self.root_path = ''
        self.infotext = '------开始------\n当前路径: ' + self.root_path + '\n'

    def createWidgets(self):
        self.lab1 = Label(self, text='目标路径:')
        self.lab1.grid(row=0, column=0)
        self.entry = Entry(self, textvariable=self.path)
        self.entry.grid(row=0, column=1)
        self.btn1 = Button(self, text='路径选择', command=self.selectPath)
        self.btn1.grid(row=0, column=2)
        self.btn2 = Button(self, text='开始转换', command=self.main)
        self.lab2 = Message(self, text=self.info, textvariable=self.info)
        self.radiobtn = Checkbutton(
            self, text='是否修改txt文件\n(默认不修改,慎重选择)', variable=self.v)

    def selectPath(self):
        path_ = tkinter.filedialog.askdirectory(
            initialdir=os.getcwd(), title="选择文件夹:")
        if path_ != '':
            text = "您选择的文件是："+path_
            self.root_path = path_
            self.path.set(text)
            self.btn2.grid(row=1, column=1)
            self.radiobtn.grid(row=1, column=0)
        else:
            self.path.set('您没有选择任何文件')

    def main(self):
        self.infotext = '-------开始-------\n当前路径: ' + self.root_path + '\n'

        self.lab2.grid(row=2, columnspan=3)
        self.info.set(self.infotext)

        for i in os.listdir(self.root_path):
            if os.path.isfile(os.path.join(self.root_path, i)) == True:
                if i.find('.jpg') > 0 or i.find('.JPG') > 0 or i.find('.PNG') > 0 or i.find('.png') > 0:
                    if re.match('[0-9]{8}', i):
                        index = i.find('.')
                        extName = i[index+1:]
                        oldName = i[0:index]
                        oldName = oldName.ljust(10, "0")  # 补齐十位
                        # newname = datetime.fromtimestamp(
                        #     int(oldName)).strftime("%Y-%m-%d_%H/%M/%S")
                        # newname = str(datetime.fromtimestamp(
                        #     int(oldName)))

                        os.rename(os.path.join(self.root_path, i),
                                  os.path.join(self.root_path, newname+'.'+extName))

                        self.infotext += '\n------图片处理------'
                        thetxt = '\n {} -> {}.{}'.format(i, newname, extName)
                        self.infotext += thetxt
                        self.info.set(self.infotext)
                    else:
                        self.infotext += '\n没有需要转换的图片'
                        self.info.set(self.infotext)
                elif self.v.get() == 1 and i.find('.TXT') > 0 or i.find('.txt') > 0:
                    filepath = os.path.join(self.root_path, i)
                    self.edit(filepath)

    def edit(self, path):
        self.infotext += '\n------TXT处理------\n'
        self.info.set(self.infotext)
        datalist = []

        with open(path, 'r+') as f:
            text = f.read()
            l = text.splitlines()

            for i in l:
                print('当前行', i)
                if(re.search(r'([0-9]{10})', i)):
                    timetamp = re.search(r'([0-9]{10})', i).group(1)

                    newname = datetime.fromtimestamp(
                        int(timetamp)).strftime("%Y-%m-%d %H:%M:%S")
                    newData = re.sub(timetamp, newname, i)
                    datalist.append(newData)

                    # data = json.loads(i)
                    # pack = json.dumps(data['package'])
                    # timetamp = re.search(r'"([0-9]+)"', pack).group(1)
                    # newname = datetime.fromtimestamp(
                    #     int(timetamp)).strftime("%Y-%m-%d %H:%M:%S")
                    # newData = re.sub(timetamp, newname, pack)

                    # data['package'] = newData
                    # datalist.append(data)
                else:
                    self.infotext += 'TXT文件没有需要转换的内容'
                    self.info.set(self.infotext)
        with open(path, 'w+') as f:
            for i in datalist:
                text = json.dumps(i)
                f.write(str(i) + '\r')
            thetxt = '\n 文件:::{} 处理完成'.format(path)
            self.infotext += thetxt
            self.info.set(self.infotext)


app = Application()
app.master.title('时间戳转换')
app.mainloop()
