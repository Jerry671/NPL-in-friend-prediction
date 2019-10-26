import tkinter as tk
root = tk.Tk()
root.title("link prediction")
lst = ["adfdasgg", "asdgsaga", "dsagsag"]
list_box = tk.Listbox(root)

for i in lst:
    list_box.insert(0, i)
list_box.pack()
root.mainloop()