import serial, threading, time
from tkinter import *

global x,y
x=0
y=0

arduino=serial.Serial('COM4',9600)
time.sleep(2)

class GUI():
    def _init_(self):
        pass
    def CrearVentana(self):
        self.ventana=Tk()
        self.label=Label(self.ventana,text=" ")
        self.label.grid(row=0,column=1)
        self.b1=Button(self.ventana,text=" ON/OFF Led", command=self.led)
        self.b1.grid(row=0,column=0)
        self.b2=Button(self.ventana,text=" Cerrar ", command=self.cerrar)
        self.b2.grid(row=0,column=2)
        hilolabel=threading.Thread(target=potenciometro)
        hilolabel.run()

    def led (self):
        global x
        if(x==0):
            arduino.write('s'.encode())
            x=1
        else:
            arduino.write('n'.encode())
            x=0

    def cerrar (self):
        arduino.close()
        self.ventana.destroy()

def potenciometro ():
    global y
    arduino.flushInput()
    dato=arduino.readline()
    y=int(dato.decode())*5.0/1023
    v.label.config(text=str(y))
    v.ventana.update()
    v.ventana.after(10,potenciometro)

def comenzar():
    v.CrearVentana()

v=GUI()
hilogui=threading.Thread(target=comenzar)
hilogui.run()
