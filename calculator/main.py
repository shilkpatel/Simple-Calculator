import tkinter
from view import CalculatorView
from model import CalculatorModel
from controller import CalculatorController

root = tkinter.Tk()
root.geometry('300x500')
CalcView = CalculatorView(root)
CalcModel = CalculatorModel()
CalcController= CalculatorController(CalcModel,CalcView)
CalcView.set_controller(CalcController)
root.mainloop()