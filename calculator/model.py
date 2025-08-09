

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
        

    def shunting_yard_algorithm(self,equation):
        stack=[]
        queue=[]
        equation = list(equation)
        tokens =[equation[0]]
        equation.pop(0)

        # This code merges multi number numbers eg 10 would be seen as ["1","0"]
        # This would connect them
        for i in equation:
            if i.isnumeric() and tokens[-1].isnumeric():
                tokens[-1]+=i
            else:
                tokens.append(i)



        for i in tokens:
            if i.isnumeric():
                queue.append(i)
            elif i == ")":
                while stack[-1]!="(":
                    queue.append(stack.pop())
                stack.pop()
            elif i in ["*","-","+","/","("]:
                stack.append(i)

        for i in range(len(stack)):
            queue.append(stack.pop())


        return self.evaluate_RPN(queue)


        
    def evaluate_RPN(self,rpn):
        stack = []

        while len(rpn)>0:
            token = rpn.pop(0)

            if token.isnumeric():
                stack.append(token)
                continue
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                
                if token == "*":
                    stack.append(left*right)
                elif token == "+":
                    stack.append(left+right)
                elif token == "-":
                    stack.append(left-right)
                elif token == "/" :
                    stack.append(left/right)
        
        return stack[0]

            





    


