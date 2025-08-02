import tkinter as tk

class CalculatorView:
    def __init__(self,root):
        self.root=root
        root.title("Calculator")

        
        input_text= tk.Text(root,height=1,width=6)
        input_text.grid(row=0,column=0,columnspan=3)

        button0 = tk.Button(root,text="0")
        button0.grid(column=1,row=4)

        button1 = tk.Button(root,text="1")
        button1.grid(column=0,row=1)

        button2 = tk.Button(root,text="2")
        button2.grid(column=1,row=1)

        button3 = tk.Button(root,text="3")
        button3.grid(column=2,row=1)

        button4 = tk.Button(root,text="4")
        button4.grid(column=0,row=2)

        button5 = tk.Button(root,text="5")
        button5.grid(column=1,row=2)

        button6 = tk.Button(root,text="6")
        button6.grid(column=2,row=2)

        button7 = tk.Button(root,text="7")
        button7.grid(column=0,row=3)

        button8 = tk.Button(root,text="8")
        button8.grid(column=1,row=3)

        button9 = tk.Button(root,text="9")
        button9.grid(column=2,row=3)

        mult = tk.Button(root,text="x")
        mult.grid(column=3,row=1)

        self.add = tk.Button(root,text="+")
        self.add.grid(column=3,row=2)

        self.div = tk.Button(root,text="/")
        self.div.grid(column=3,row=3)

        self.sub = tk.Button(root,text="-")
        self.sub.grid(column=3,row=4)

        
