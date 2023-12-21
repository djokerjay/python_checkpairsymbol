class Symbol:
    def __init__(self,opensymbol,closesymbol):
        self.opensymbol = opensymbol
        self.closesymbol = closesymbol
        self.opencount = 0
        self.closecount =0
    def addCount(self,symbol):
        if symbol==self.opensymbol:
            self.opencount = self.opencount +1
        else:
            self.closecount = self.closecount +1         

def addCount(symbols,symbol):
    for i in range(len(symbols)):
        if symbols[i].opensymbol == symbol or symbols[i].closesymbol == symbol:
            symbols[i].addCount(symbol)

def parse(symbols,input):
    for i in range(len(input)):
        char = input[i]
        if char == "/":
            if (i+1) <= (len(input)-1):
                char2 = input [i+1]
                if(char2=="*"):
                    addCount(symbols,char+char2)
                    i=i+2
        elif char == "*":
            if (i+1) <= (len(input)-1):
                char2 = input [i+1]
                if(char2=="/"):
                    addCount(symbols,char+char2)
                    i=i+2
        else:
            addCount(symbols,char)

def main():
    Symbols=[]
    Symbols.append(Symbol("{","}"))
    Symbols.append(Symbol("[","]"))
    Symbols.append(Symbol("(",")"))
    Symbols.append(Symbol("/*","*/"))
    text  = input("Enter Text:")
    parse(Symbols,text)
    result = True
    for i in range(len(Symbols)):
        symbol = Symbols[i]
        print("Open:" , symbol.opensymbol , "(", symbol.opencount ,")" ,">>Close:" , symbol.closesymbol, "(", symbol.closecount ,")" )
        if(symbol.opencount != symbol.closecount):
            result = False
    if result==True:
        print("Success")
    else:
        print("Failed")    
        
main()
