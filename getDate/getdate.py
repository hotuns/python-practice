# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   getdate.py
@Time    :   2019/07/15 13:33:22
'''


from datetime import datetime
import os
import json
import re

# 需要修改的图片路径, 默认是当前路径
root_path = './'


def main():
    for i in os.listdir(root_path):
        if not i == 'getdate.py':
            if os.path.isfile(os.path.join(root_path, i)) == True:
                if i.find('.jpg') > 0:
                    index = i.find('.')
                    extName = i[index+1:]
                    oldName = i[0:index]
                    newname = datetime.fromtimestamp(
                        int(oldName)).strftime("%Y-%m-%d %H:%M:%S")

                    os.rename(os.path.join(root_path, i),
                              os.path.join(root_path, newname+'.'+extName))
                    print(i,  '->', newname+'.'+extName)
                elif i.find('.TXT') > 0:
                    filepath = os.path.join(root_path, i)
                    edit(filepath)


def edit(path):
    datalist = []

    with open(path, 'r+') as f:
        text = f.read()
        l = text.splitlines()

        for i in l:
            data = json.loads(i)
            pack = json.dumps(data['package'])
            timetamp = re.search(r'"([0-9]+)"', pack).group(1)
            newname = datetime.fromtimestamp(
                int(timetamp)).strftime("%Y-%m-%d %H:%M:%S")
            newData = re.sub(timetamp, newname, pack)

            data['package'] = newData
            datalist.append(data)

    with open(path, 'w+') as f:
        for i in datalist:
            text = json.dumps(i)
            f.write(str(i) + '\r')
        print(path + 'done')


main()
