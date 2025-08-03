

class CalculatorController:
    def __init__(self,model,view):
        self.model = model
        self.view = view



    def NumMap(self,num):
        self.view.input_text.insert("end-1c",num)

    def multMap(self):
        self.view.input_text.insert("end-1c","*")

    def addMap(self):
        self.view.input_text.insert("end-1c","+")

    def subMap(self):
        self.view.input_text.insert("end-1c","-")

    def divMap(self):
        self.view.input_text.insert("end-1c","/")

    def equalMap(self):
        answer = self.model.equal(self.view.input_text.get("1.0",'end-1c'))
        self.view.input_text.delete(1.0,"end-1c")
        self.view.input_text.insert("end-1c",str(answer))

    def back(self):
        current = self.view.input_text.get("1.0",'end-1c')
        if current=="":
            return
        self.view.input_text.delete(1.0,"end-1c")
        self.view.input_text.insert("end-1c",current[:-1])
