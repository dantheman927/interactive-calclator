class calfunctions:
    def add(x, y):
        print(x + y)

    def sub(x, y):
        print(x - y)

    def tim(x, y): 
        print(x * y)

    def div(x, y):
        print(x / y)

    def squ(x):
        print(x * x)

cf = calfunctions

while True:
    def calculor(caltype):
            try:
                
                
                caltype = caltype.split(" ")
                
                
                while (caltype.count("")):
                    caltype.remove("") 

                
                cal0 = int(caltype[0])
                if "^" != caltype[1]:  
                    cal2 = int(caltype[2])
            
                
                if caltype[1] in ["+", "add"]:
                    cf.add(cal0, cal2)
                elif caltype[1] in ["-", "sub"]:
                    cf.sub(cal0, cal2)
                elif caltype[1] in ["*", "times"]:
                    cf.tim(cal0, cal2)
                elif caltype[1] in ["/", "div"]:
                    cf.div(cal0, cal2)
                elif caltype[1] == "^":
                    cf.squ(cal0)

            
            except ValueError:
                print("Please enter a valid calculation, like '5 + 5' or '4 ^' for square.")

        

    calinput = input("Enter what you want to calculate, e.g.,'5 + 5' or '4 ^' for square:\n")
    calculor(calinput)

