# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

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
            datalist.append(i)

    with open('./README.md', 'a+') as f:
        data = f.read()
        for i in datalist:
            mdText = '''
            \n* [{}]({}/{}) \n
                描述
            '''.format(i, githubRootUrl, i)
            if data.find(i) == -1:
                f.write(mdText)
                print('添加{} '.format(i))


if __name__ == "__main__":
    main()
