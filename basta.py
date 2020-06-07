import serial, threading, time
from tkinter import *
from random import randint


global ent, total, letra, x,y, t1, t2, t3, t4, t5, NOMBRE, APELLIDO, CIUDAD, FLOR, COSA,control,control2,control3
total=0
ent=0
x=64
y=0
control=0
control2=0
control3=0

t1="A"
t2="A"
t3="A"
t4="A"
t5="A"

arduino=serial.Serial('COM4',9600)
time.sleep(2)

def comenzar():
    v.CrearVentana()



class basta():
    def _init_(self):
        pass
    def CrearVentana(self):
        global NOMBRE, APELLIDO, CIUDAD, FLOR, COSA
        self.ventana=Tk()
        self.ventana.geometry("700x500")
        
        self.i=PhotoImage(file="bast.gif")
        self.I=Label(self.ventana, image=self.i)
        self.I.place(x=45,y=10)
        
        self.label=Label(self.ventana,text="Juego de basta",font="arial 18",bg="gold",fg="black")
        self.label.place(x=225,y=0,width=200,height=50)

        self.labelletra=Label(self.ventana,text=" ",font="arial 18",bg="white",fg="black")
        self.labelletra.place(x=425,y=0,width=50,height=50)
       
        self.label1=Label(self.ventana,text="NOMBRE",font="arial 18",fg="black")
        self.label1.place(x=0,y=100,width=200,height=50)
        
        self.label2=Label(self.ventana,text="APELLIDO",font="arial 18",fg="black")
        self.label2.place(x=0,y=150,width=200,height=50)
        
        self.label3=Label(self.ventana,text="CIUDAD/PAIS",font="arial 18",fg="black")
        self.label3.place(x=0,y=200,width=200,height=50)
        
        self.label4=Label(self.ventana,text="FLOR/FRUTO",font="arial 18",fg="black")
        self.label4.place(x=0,y=250,width=200,height=50)
        
        self.label5=Label(self.ventana,text="COSA",font="arial 18",fg="black")
        self.label5.place(x=0,y=300,width=200,height=50)

        self.label6=Label(self.ventana,text="puntuacion: ",font="arial 18",fg="black")
        self.label6.place(x=0,y=350,width=200,height=50)
        
        self.label7=Label(self.ventana,text=" ",font="arial 18",fg="black")
        self.label7.place(x=250,y=350,width=150,height=50)

        self.label8=Label(self.ventana,text="Para seguir jugando presione INICIO",font="arial 24",fg="black")
        self.label8.place(x=100,y=450)
        
        
        NOMBRE=StringVar()
        self.nombre=Entry(self.ventana,textvariable=NOMBRE,font="arial 12",state=DISABLED,bd=3)
        self.nombre.place(x=250,y=100,width=200,height=50)
        
        APELLIDO=StringVar()
        self.apellido=Entry(self.ventana,textvariable=APELLIDO,font="arial 12",state=DISABLED,bd=3)
        self.apellido.place(x=250,y=150,width=200,height=50)
        
        CIUDAD=StringVar()
        self.ciudad=Entry(self.ventana,textvariable=CIUDAD,font="arial 12",state=DISABLED,bd=3)
        self.ciudad.place(x=250,y=200,width=200,height=50)

        FLOR=StringVar()
        self.flor=Entry(self.ventana,textvariable=FLOR,font="arial 12",state=DISABLED,bd=3)
        self.flor.place(x=250,y=250,width=200,height=50)

        COSA=StringVar()
        self.cosa=Entry(self.ventana,textvariable=COSA,font="arial 12",state=DISABLED,bd=3)
        self.cosa.place(x=250,y=300,width=200,height=50)
        
        hilolabel=threading.Thread(target=on_off_game)
        hilolabel.run()

    def obtener(self):
        global t1, t2, t3, t4, t5

        t1=NOMBRE.get()
        t2=APELLIDO.get()
        t3=CIUDAD.get()
        t4=FLOR.get()
        t5=COSA.get()
        if(len(t1)==0):
            t1=chr(0)
        if(len(t2)==0):
            t2=chr(0)
        if(len(t3)==0):
            t3=chr(0)
        if(len(t4)==0):
            t4=chr(0)
        if(len(t5)==0):
            t5=chr(0)


def on_off_game():
    global ent,control,control2,control3
    
    arduino.flushInput()
    dato=arduino.readline()
    ent=int(dato.decode())

    
    if(ent==1 and control2==0):
        
        letra_random()
        
        v.label.config(text="INICIO")
        v.nombre.config(state=NORMAL)
        v.apellido.config(state=NORMAL)
        v.ciudad.config(state=NORMAL)
        v.cosa.config(state=NORMAL)
        v.flor.config(state=NORMAL)
        v.label8.place_forget()
        
        control=0
        control2=1
        control4=0
        
    if(ent==2 and control==0):
        
        control=1
        
        v.obtener()
        verificar()
        
        v.label.config(text="BASTA!")
        v.nombre.config(state=DISABLED)
        v.apellido.config(state=DISABLED)
        v.ciudad.config(state=DISABLED)
        v.cosa.config(state=DISABLED)
        v.flor.config(state=DISABLED)
        v.label8.place(x=100,y=450)
        
    if(ent==3):
        finalizar()

    if(control3==0):
        v.ventana.update()
        v.ventana.after(10,on_off_game)


def letra_random():
    global letra,x
    x=randint(65,90)
    letra=chr(x)
    v.labelletra.config(text=letra)

def verificar():
    global letra, NOMBRE, APELLIDO, FLOR, CIUDAD, COSA, x, y, total,control,control2
    y=x+32
    if(x==ord(t1[0]) or (y==ord(t1[0]) and ord(t1[0])<123) ):
        total+=100

    if(x==ord(t2[0]) or (y==ord(t2[0]) and ord(t2[0])<123) ):
        total+=100

    if(x==ord(t3[0]) or (y==ord(t3[0]) and ord(t3[0])<123) ):
        total+=100

    if(x==ord(t4[0]) or (y==ord(t4[0]) and ord(t4[0])<123) ):
        total+=100

    if(x==ord(t5[0]) or (y==ord(t5[0]) and ord(t5[0])<123) ):
        total+=100

    v.label7.config(text=total)
    control2=0

def finalizar():
    global control3
    control3=1
    arduino.close()
    v.ventana.destroy()

v=basta()
hilobasta=threading.Thread(target=comenzar)
hilobasta.run()
