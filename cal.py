class calfunctions:
    def add(x,y):
        print(x+y)

    def sub(x,y):
        print(x-y)

    def tim(x,y): 
        print(x*y)

    def div(x,y):
        print(x/y)

    def squ(x):
        print(x * x)

cf = calfunctions

def calculor(caltype):
    
    caltype = caltype.split(" ")
    
    while (caltype.count("")):
        caltype.remove("") 


    cal0 = int(caltype[0])
    if "^"  != caltype[1]:
        cal2 = int(caltype[2])
    
    if caltype[1] in ["+","add"]:
       cf.add(cal0,cal2)
    elif caltype[1] in ["-","sub"]:
        cf.sub(cal0,cal2)
    elif caltype[1] in ["*","times"]:
        cf.tim(cal0,cal2)
    elif caltype[1] in ["/","div"]:
       cf.div(cal0,cal2)
    elif caltype[1] in ["^"]:        
        cf.squ(cal0)

calinput = input("enter a what you want e.g 5 + 5\n")

calculor(calinput)

