from tkinter import Tk, Button, Entry, StringVar, messagebox # Objetos para crear nuestra ventana
from operator import add, sub,  mul, truediv # Realizar operaciones basicas
import re # Validar numeros mediante expresiones regulares

class Calculadora:
    def __init__(self):
        self.ventana = Tk()  # Objeto para crear la ventana
        self.ventana.title("Calculadora taller Python")  # titulo de la ventana
        self.ventana.geometry("400x375")  # dimension de la ventana (Ancho x Largo)
        self.ventana.resizable(width=False, height=False)  # configurar que la ventana no sea redimensionable
        self.texto_display = StringVar()
        self.display = Entry(self.ventana, font=('arial',20,'bold'), width=22, borderwidth=10,
                             background="CadetBlue1", textvariable=self.texto_display)
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
        self.operador = ""
        ancho_boton = 10
        alto_boton = 3
        self.boton_9 = Button(self.ventana, text='9', width=ancho_boton,
                              height=alto_boton, command=lambda: self.imprimir('9'))
        self.boton_9.grid(row=1, column=0, pady = 5)
        self.boton_8 = Button(self.ventana, text='8', width=ancho_boton,
                              height=alto_boton, command=lambda: self.imprimir('8'))
        self.boton_8.grid(row=1, column=1, pady=5)
        self.boton_7 = Button(self.ventana, text='7', width=ancho_boton,
                              height=alto_boton, command=lambda: self.imprimir('7'))
        self.boton_7.grid(row=1, column=2, pady=5)
        self.boton_add = Button(self.ventana, text='+', width=ancho_boton,
                              height=alto_boton, command=lambda: self.imprimir('+'))
        self.boton_add.grid(row=1, column=3, pady=5)
        self.boton_6 = Button(self.ventana, text='6', width=ancho_boton,
                              height=alto_boton, command=lambda: self.imprimir('6'))
        self.boton_6.grid(row=2, column=0, pady=5)
        self.boton_5 = Button(self.ventana, text='5', width=ancho_boton,
                              height=alto_boton, command=lambda: self.imprimir('5'))
        self.boton_5.grid(row=2, column=1, pady=5)
        self.boton_4 = Button(self.ventana, text='4', width=ancho_boton,
                              height=alto_boton, command=lambda: self.imprimir('4'))
        self.boton_4.grid(row=2, column=2, pady=5)
        self.boton_sub = Button(self.ventana, text='-', width=ancho_boton,
                                height=alto_boton, command=lambda: self.imprimir('-'))
        self.boton_sub.grid(row=2, column=3, pady=5)
        self.boton_3 = Button(self.ventana, text='3', width=ancho_boton,
                              height=alto_boton, command=lambda: self.imprimir('3'))
        self.boton_3.grid(row=3, column=0, pady=5)
        self.boton_2 = Button(self.ventana, text='2', width=ancho_boton,
                              height=alto_boton, command=lambda: self.imprimir('2'))
        self.boton_2.grid(row=3, column=1, pady=5)
        self.boton_1 = Button(self.ventana, text='1', width=ancho_boton,
                              height=alto_boton, command=lambda: self.imprimir('1'))
        self.boton_1.grid(row=3, column=2, pady=5)
        self.boton_mul = Button(self.ventana, text='*', width=ancho_boton,
                                height=alto_boton, command=lambda: self.imprimir('*'))
        self.boton_mul.grid(row=3, column=3, pady=5)
        self.boton_0 = Button(self.ventana, text='0', width=ancho_boton,
                              height=alto_boton, command=lambda: self.imprimir('0'))
        self.boton_0.grid(row=4, column=0, pady=5)
        self.boton_eq = Button(self.ventana, text='=', width=ancho_boton,
                              height=alto_boton, command=self.operacion)
        self.boton_eq.grid(row=4, column=1, pady=5)
        self.boton_clear = Button(self.ventana, text='clear', width=ancho_boton,
                              height=alto_boton, command=self.limpiar_display)
        self.boton_clear.grid(row=4, column=2, pady=5)
        self.boton_div = Button(self.ventana, text='/', width=ancho_boton,
                                height=alto_boton, command=lambda: self.imprimir('/'))
        self.boton_div.grid(row=4, column=3, pady=5)

    def imprimir(self, numero):
        self.operador += numero
        self.texto_display.set(self.operador)

    def limpiar_display(self):
        self.operador = ""
        self.texto_display.set("")

    def validar_numero(self):
        validar = r'[0-9]*.{0,1}[0-9]*'

    def operacion(self):
        try:
            resultado = eval(self.operador)
        except:
            resultado = "Error"
        self.texto_display.set(resultado)

    def encender(self):
        self.ventana.mainloop()

if __name__ == '__main__':
    mi_calculadora = Calculadora()
    mi_calculadora.encender()
