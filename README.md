# Network-relation-prediction
通过人际关系网络预测任意两个人为好友的可能性

## 项目介绍
基于开源项目linkpred实现网络关系的预测
<br>用户可以通过修改path(训练集)预测不同人际关系网络之间的好友关系可能性
<br>每次预测显示四组人之间的好友关系可能性，通过点击NEXT按钮进行下一组预测
<br>支持python3.+版本
## 使用说明
默认使用斯坦福大学的soc-pokec-relationships数据集进行训练，详情参考项目介绍
<br>编译运行GUIshow.py，将会显示如下图的结果
<br>其中前两列代表人物标号，第三列为两人可能为好友关系的概率
### 使用到的开源项目
[linkpred](https://github.com/rafguns/linkpred)

### 项目主要功能实现代码
////////////////////////////////////////////////////////////////////////////////////////
<br>import tkinter as tk
<br>import sys
<br>root = tk.Tk()
<br>path = r'soc-pokec-relationships_sub-CommonNeighbours-predictions_2019-10-27_21.30.txt'
<br>lst = []
<br>f = open(path, "r")
<br>for line in f:
    <br>subList = line.replace('\n', '').split('\t')
<br>lst.append(subList)
<br>f.close()
<br>for i in range(20):
    <br>sys.stdout.write(str(lst[i]) + '\n')
<br>sys.stdout.write("list is done")
<br>root.title("link prediction")
<br>list_box = tk.Listbox(root)
<br>def go():
    <br>sys.stdout.write("changed\n")
    <br>for i in range(4):  # 每次多显示4个
        <br>>list_box.delete(8)
        <br>>slist = lst.pop(0)
        <br>>str = slist[0] + '   ' + slist[1] + '   ' + slist[2]
        <br>>list_box.insert(0,str)
<br>but = tk.Button(root,text='next',bg='white', command=go)
<br>for i in range(8):
    <br>slist = lst.pop(0)
    <br>str = slist[0] + '   ' + slist[1] + '   ' + slist[2]
    <br>list_box.insert(0, str)
<br>list_box.pack()
<br>but.pack()
<br>root.mainloop()
<br>////////////////////////////////////////////////////////////////////////////////////////
