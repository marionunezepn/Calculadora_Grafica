from tkinter import *
class calculadora:
    def __init__(self,master):
        self.frame=Frame(master)
        self.frame.grid()
        self.pantalla=Entry(master,width=35)
        self.pantalla.grid(row=10,column=0)
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
            if self.pantalla.get()[0] not in todo:
                self.pantalla.insert(END,"Operacion novalida")
            try:
                resultado=eval(self.pantalla.get())
                self.pantalla.insert(END,"="+str(resultado))
            except:
                self.pantalla.insert(END,"Error")
        elif valor=="C":
            self.pantalla.delete(0,END)
        else:
            if "=" in self.pantalla.get():
                self.pantalla.delete(0,END)
            self.pantalla.insert(END,valor)

root=Tk()
root.title("CALCULADORA")
root.geometry('200x200+10+10')
root.resizable(width=TRUE, height=TRUE)
calculadora(root)
root.mainloop()



