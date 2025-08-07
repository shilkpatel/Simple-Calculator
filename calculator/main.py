import tkinter
from calculator.view import CalculatorView
from calculator.model import CalculatorModel
from calculator.controller import CalculatorController

root = tkinter.Tk()
root.geometry('300x500')
CalcView = CalculatorView(root)
CalcModel = CalculatorModel()
CalcController= CalculatorController(CalcModel,CalcView)
CalcView.set_controller(CalcController)
root.mainloop()