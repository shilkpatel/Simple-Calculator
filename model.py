

class CalculatorModel:
    def __init__(self):
        self.value = None
        self.value2 = None
        self.ans = None
        self.state= "num1"
        # opp , num2

        self.opp = None

    def equal(self,equation):
        if "*" in equation:
            equation = equation.split("*")
            return float(equation[0]) * float(equation[1])
        elif "+" in equation:
            equation = equation.split("+")
            return float(equation[0]) + float(equation[1])
        elif "-" in equation:
            equation = equation.split("-")
            return float(equation[0]) - float(equation[1])
        elif "/" in equation:
            equation = equation.split("/")
            return float(equation[0]) / float(equation[1])


    


