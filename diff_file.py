#coding:utf-8

import difflib

def betweenDiff(fileone,filetwo):
    with open(fileone) as f:
        lines = f.readlines()

    with open(filetwo) as f:
        new_lines = f.readlines()

    d = difflib.HtmlDiff()
    html = d.make_file(lines,new_lines)

    return html

if __name__ == '__main__':
    fileone = '/root/PythonProjects/jiankong/test1.txt'
    filetwo = '/root/PythonProjects/jiankong/test.txt'
    html = betweenDiff(fileone,filetwo)
    print(html)