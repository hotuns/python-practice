# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
执行之后会自动更新该项目的README
名字: 根据文件夹名
描述: 根据index文件头部的描述信息
'''
import os
# 之类本来想跳转到上级目录, 后来想想直接在上级目录运行这个文件就行了
# root_path = os.path.abspath(os.path.join(os.getcwd(), '../'))
root_path = os.getcwd()
githubRootUrl = 'https://github.com/hedongshu/python-practice'

print("工作目录", root_path)


def main():
    datalist = []
    for i in os.listdir(root_path):
        if(os.path.isdir(i) and i.find('.') == -1):
            dataObj = {
                'describe': '暂无描述',
                'name': i
            }

            # 读取注释
            filePath = os.path.join(root_path, i, 'index.py')
            with open(filePath) as f:
                startIndex = None
                endIndex = None
                lines = f.readlines()
                for index, line in enumerate(lines):
                    if endIndex == None:
                        if line.startswith("'''"):
                            if startIndex == None:
                                startIndex = index
                            else:
                                endIndex = index
                print(startIndex, endIndex)

                # 读取描述信息
                thedescribe = ''
                for i in range(startIndex+1, endIndex):
                    text = lines[i]
                    if(not text.startswith('@')):
                        thedescribe += text
                dataObj['describe'] = thedescribe

            datalist.append(dataObj)

    with open('./README.md', 'w+') as f:
        data = f.read()

        startText = '''# python-practice

记录一下使用python写的一些东西



---'''
        f.write(startText)
        for i in datalist:
            mdText = '''\n* [{}]({}/{}) \n    {}'''.format(i['name'],
                                                           githubRootUrl, i['name'], i['describe'])
            if data.find(i['name']) == -1:
                f.write(mdText)
                print('添加{} '.format(i))
        f.close()


if __name__ == "__main__":
    main()
