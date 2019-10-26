import tkinter as tk
root = tk.Tk()

root.title("link prediction")
lst = ["adfdasgg", "asdgsaga", "dsagsag"]
list_box = tk.Listbox(root)

def go():
    print("yes")
    for i in range(4):  # 每次多显示4个
        list_box.delete(8)
        list_box.insert(0,"yes")


but = tk.Button(root,text='next',bg='white', command=go)

for i in lst:
    list_box.insert(0, i)
list_box.pack()
but.pack()
root.mainloop()