import regex

INTEGER = "[0-9]+"

OPERATOR = "[+|-|*|/]"




PAIR ="(?:"+ INTEGER + OPERATOR + INTEGER +")" +\
"|(?:"+"[\((?:?R)\)]"+ OPERATOR + INTEGER + ")"+\
"|(?:"+INTEGER + OPERATOR + "[\((?:?R)\)]" + ")"+\
"|(?:"+ "[\((?:?R)\)]" + OPERATOR + "[\((?:?R)\)]" +")"\
"|[\((?:?R)\)]"



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
    '''
    def equalMap(self):
        answer = self.model.equal(self.view.input_text.get("1.0",'end-1c'))
        self.view.input_text.delete(1.0,"end-1c")
        self.view.input_text.insert("end-1c",str(answer))
    '''
    def equalMap(self):
        
        # Input santization here
        print(self.view.input_text.get("1.0",'end-1c'))
        print(regex.findall(PAIR,self.view.input_text.get("1.0",'end-1c')))

        if regex.findall(PAIR,self.view.input_text.get("1.0",'end-1c')):
            print("Match")
            answer = self.model.shunting_yard_algorithm(self.view.input_text.get("1.0",'end-1c'))
            self.view.input_text.delete(1.0,"end-1c")
            self.view.input_text.insert("end-1c",str(answer))
        else:
            print("No Match")

        

    def back(self):
        current = self.view.input_text.get("1.0",'end-1c')
        if current=="":
            return
        self.view.input_text.delete(1.0,"end-1c")
        self.view.input_text.insert("end-1c",current[:-1])
