

class CalculatorController:
    def __init__(self,model,view):
        self.model = model
        self.view = view



    def NumMap(self,num):
        print(num)
        res = self.model.number(num)
        print(self.model.value)
        print(self.model.value2)
        
        self.view.input_text.insert("end-1c",res)

    def multMap(self):
        self.model.mult()
        self.view.input_text.delete(1.0,"end-1c")

    def equalMap(self):
        answer = self.model.equal()
        self.view.input_text.delete(1.0,"end-1c")
        self.view.input_text.insert("end-1c",str(answer))