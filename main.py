import tkinter
from view import CalculatorView
from model import CalculatorModel
from controller import CalculatorController

root = tkinter.Tk()
CalcView = CalculatorView(root)
CalcModel = CalculatorModel()
CalcController= CalculatorController(CalcModel,CalcView)
CalcView.set_controller(CalcController)
root.mainloop()