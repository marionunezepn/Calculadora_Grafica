from tkinter import *
class calculadora:
    def __init__(self,master):
        self.frame=Frame(master)
        self.frame.grid()
        bts=["0","1","2","3","4","5","6","7","8","9","+","-","=","*","/","C"]
        r=1
        c=0
        for bt in bts:
            comando=lambda x=bt:self.calcular(x)
            self.boton=Button(self.frame,text=bt,width=4,height=2,command=comando)
            self.boton.grid(row=r,column=c)
            c +=1
            if c>3:
                c=0
                r +=1

    def calcular(self,valor):
        if valor=="=":
            todo="123456789+-*/"
            try:
                resultado=eval(self.dados.get())
            except:
        elif valor=="C":
        else:

root=Tk()
root.title("CALCULADORA")
root.geometry('200x200+10+10')
root.resizable(width=TRUE, height=TRUE)
calculadora(root)
root.mainloop()



