import tkinter as tk

class CalculatorView:
    def __init__(self,root):
        self.root=root
        root.title("Calculator")

        
        self.input_text= tk.Text(root,height=1,width=6)
        self.input_text.grid(row=0,column=0,columnspan=3)

        self.button0 = tk.Button(root,text="0")
        self.button0.grid(column=1,row=4)

        self.button1 = tk.Button(root,text="1")
        self.button1.grid(column=0,row=1)

        self.button2 = tk.Button(root,text="2")
        self.button2.grid(column=1,row=1)

        self.button3 = tk.Button(root,text="3")
        self.button3.grid(column=2,row=1)

        self.button4 = tk.Button(root,text="4")
        self.button4.grid(column=0,row=2)

        self.button5 = tk.Button(root,text="5")
        self.button5.grid(column=1,row=2)

        self.button6 = tk.Button(root,text="6")
        self.button6.grid(column=2,row=2)

        self.button7 = tk.Button(root,text="7")
        self.button7.grid(column=0,row=3)

        self.button8 = tk.Button(root,text="8")
        self.button8.grid(column=1,row=3)

        self.button9 = tk.Button(root,text="9")
        self.button9.grid(column=2,row=3)

        self.mult = tk.Button(root,text="x")
        self.mult.grid(column=3,row=1)

        self.add = tk.Button(root,text="+")
        self.add.grid(column=3,row=2)

        self.div = tk.Button(root,text="/")
        self.div.grid(column=3,row=3)

        self.sub = tk.Button(root,text="-")
        self.sub.grid(column=3,row=4)

        self.equal = tk.Button(root,text="=")
        self.equal.grid(column=4,row=4)

        self.controller= None

    
    def set_controller(self,controller):
        self.controller = controller



        self.mult.config(command=self.controller.multMap)

        self.button0.config(command=lambda:self.controller.NumMap(0))
        self.button1.config(command=lambda:self.controller.NumMap(1))
        self.button2.config(command=lambda:self.controller.NumMap(2))
        self.button3.config(command=lambda:self.controller.NumMap(3))
        self.button4.config(command=lambda:self.controller.NumMap(4))
        self.button5.config(command=lambda:self.controller.NumMap(5))
        self.button6.config(command=lambda:self.controller.NumMap(6))
        self.button7.config(command=lambda:self.controller.NumMap(7))
        self.button8.config(command=lambda:self.controller.NumMap(8))
        self.button9.config(command=lambda:self.controller.NumMap(9))

        self.equal.config(command=self.controller.equalMap)