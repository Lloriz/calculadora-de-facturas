import tkinter as tk

ventana = tk.Tk()

#NOMBRE DEL PROGRAMA
ventana.title('CALCULADORA DE IMPUESTOS') 

#TAMAÑO CON EL QUE SE ABRE LA VENTANA
ventana.geometry('666x500')

#HACE QUE EL TAMAÑO DE VENTANA NO SE PUEDA MODIFICAR
ventana.resizable(width=False, height= False)

#Fondo
fondo = tk.PhotoImage(file="c:/Users/raul/Desktop/Programacion/ondocalcu3.png")
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

#Fuente


#Contenedor de las operaciones, es un string
operador=''

#El texto que se muestra en pantalla
bi_texto1 = tk.StringVar()
total_pantalla = tk.StringVar()
iva = tk.StringVar()
precio_iva1= tk.StringVar()
retencion1 = tk.StringVar()
tellevas_pantalla = tk.StringVar()

#Función CLEAR
def clear():
    total_pantalla.set('')
    iva.set('')
    precio_iva1.set('')
    retencion1.set('')
    bi_texto1.set('')
    tellevas_pantalla.set('')
    
#Función TOTAL
def total():
    valor= float(bi_caja.get())
    i = float((21*valor)/100)
    p_i = float(valor + (21*valor)/100)
    r = float((15*valor)/100)
    total = float((valor +(21*valor)/100)-(15*valor)/100)
    telle = float(((valor +(21*valor)/100)-(15*valor)/100)-(21*valor)/100)
    
    bi_texto1.set
    total_pantalla.set(total)
    iva.set(i)
    precio_iva1.set(p_i)
    retencion1.set(r)
    tellevas_pantalla.set(telle)


#Etiquetas
bi_label = tk.Label(ventana, text='Base Imponible',font=('helvetica',20,'bold'))
bi_label.grid()

iva_label = tk.Label(ventana, text='IVA 21%',font=('helvetica',20,'bold'))
iva_label.grid(row=1)

precio_iva_label = tk.Label(ventana, text='Precio con IVA',font=('helvetica',20,'bold'))
precio_iva_label.grid(row=2)

retencion_label = tk.Label(ventana, text='Retención de IRPF 15%',font=('helvetica',20,'bold'))
retencion_label.grid(row=3)

tellevas_label = tk.Label(ventana, text='Lo que te llevas limpio',font=('helvetica',20,'bold'))
tellevas_label.grid(row=5)

#Entrada de texto, base imponible
bi_caja = tk.Entry(ventana,font=('helvetica',20,'bold'),width=10,borderwidth=10,textvariable=bi_texto1)
bi_caja.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

#Caja IVA
iva_caja = tk.Entry(ventana,font=('helvetica',20,'bold'),width=10,borderwidth=10,state='disabled',textvariable=iva)
iva_caja.grid(row=1, column=1, columnspan=4, padx=10, pady=10)

#Caja precio con IVA
precio_iva_caja = tk.Entry(ventana,font=('Arial',20,'bold'),width=10,borderwidth=10,state='disabled',textvariable=precio_iva1)
precio_iva_caja.grid(row=2, column=1, columnspan=4, padx=10, pady=10)

#Caja Retencion IRPF
retencion_caja = tk.Entry(ventana,font=('helvetica',20,'bold'),width=10,borderwidth=10,state='disabled',textvariable=retencion1)
retencion_caja.grid(row=3, column=1, columnspan=4, padx=10, pady=10)

#Total Factura
total_caja = tk.Entry(ventana,font=('helvetica',20,'bold'),width=10,borderwidth=10,state='disabled',textvariable=total_pantalla)
total_caja.grid(row=4, column=1, columnspan=4, padx=10, pady=10)

#Caja Lo que te llevas
tellevas_caja = tk.Entry(ventana,font=('helvetica',20,'bold'),width=10,borderwidth=10,state='disabled',textvariable=tellevas_pantalla)
tellevas_caja.grid(row=5, column=1, columnspan=4, padx=10, pady=10)

#BOTONES
btnclear = tk.Button(ventana, text='LIMPIAR', fg='white', bg='black', height=2, width=30,border=6, command=clear).grid(row=6, column=2,pady=10)

btncalcular = tk.Button(ventana, text='IMPORTE TOTAL DE LA FACTURA', fg='white', bg='black', height=2, width=30,border=6, command=total).grid(row=4, column=0,padx=10,pady=10,)


#HACE QUE LA VENTANA NO SE CIERRE
ventana.mainloop()
