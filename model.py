

class CalculatorModel:
    def __init__(self):
        self.value = None
        self.value2 = None
        self.ans = None
        self.state= "num1"
        # opp , num2

        self.opp = None



    def number(self,num):
        if self.state == "num1":
            self.value = int(num)
            self.state = "opp"
            return num
        elif self.state == "num2":
            self.value2 = int(num)
            return num
        
        return ""

    def mult(self):
        self.opp = "mult"
        self.state = "num2"

    def equal(self):
        if self.state != "num2":
            return
        
        if self.opp =="mult":
            return self.value*self.value2


    


