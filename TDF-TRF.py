from tkinter import * #Se importa la libreria Tkinter para Interfaces graficas
from mpmath import ln, pi, cosh, sinh #Se importan estas funciones matematicas
from sympy import * #Symy permite trabajar con funciones matematicas y a parte graficar
from tkinter import scrolledtext #Es para la ventana de texto de los resultados
from tkinter import messagebox #Para las ventanas de los datos en los resultados
from math import e #Se importa e para el calculo de las transformadas
import matplotlib.pyplot as plt #Para las graficas
import math #Para calculos


ventana = Tk()  #Se crea una nueva ventana
ventana.title("Transformada Discreta/Rapida de Fourier") #Se le pone un titulo a la ventana
ventana.geometry('1000x450') #Se define un tamaño para la ventana
ventana.resizable(width=0, height=0) #Con esto hacemos que el usuario no pueda cambiar el tamaño de la ventana

#Un label para lo que necesitaremos ingresar

lbl = Label(ventana , text="Muestra (N): ", #Se ingresara la muestra que deseamos trabajas
font=("Arial Bold" , 15))

lbl.grid(column=3 , row=5)  #Para la posicion en la GUI


#Para ingrear los datos

Muestra = Entry(ventana, font=("calibri 20") , width=10)
Muestra.grid(row=5,column=5,columnspan=2,padx=4,pady=5)



#Botones

calcular_tdf = Button(ventana, text = "TDF" , width = 7, height = 2 , command = lambda:tdf())
calcular_tdf.grid(row =5 , column = 10 , padx = 15, pady = 5)

calcular_tdfi = Button(ventana, text = "Inversa TDF" , width = 9, height = 2 , command = lambda:tdfi())
calcular_tdfi.grid(row =5 , column = 11 , padx = 15, pady = 5)

calcular_trf = Button(ventana, text = "TRF" , width = 7, height = 2 , command = lambda:trf())
calcular_trf.grid(row =5 , column = 12 , padx = 15, pady = 5)

calcular_trfi = Button(ventana, text = "Inversa TRF" , width = 9, height = 2 , command = lambda:trfi())
calcular_trfi.grid(row =5 , column = 13 , padx = 15, pady = 5)



#Funciones

def tdf(): #Funcion para calcular la transformada discreta de fourier
    muestra = Muestra.get() #Se extraen el numero de la muestra de la GUI
    N = eval(muestra) #Se evalua para poder trabajarlo

    tdfr = [] #Un arreglo para guardar los resultados (Parte real)
    tdfi = [] #Un arreglo para guardar los resultados (Parte imaginaria)
    tdf = [] #Un arreglo para guardar el resultado

    for i in range(0 , N): #Un ciclo for para la sumatoia. Va de 0 a N
      res = (i)*(e**((-1j*2*3.1416*i*i)/N)) #En la variable res se guarda el resultado de la formula
      tdfr.append(re(res)) #Aqui guardamos la parte real
      tdfi.append(im(res)) #Aqui guardamos la parte imaginaria
      tdf.append(res) #Aqui guardamos todo el resultado

  

    txt = scrolledtext.ScrolledText(ventana,width=45,height=15) #Se crea la ventana para mostrar el resultado
    txt.grid(column=5,row=30)  #Para la posicion

    

    txt.insert(INSERT, "Datos(1 a N-1):") #Se muestra el mensaje en pantalla

    txt.insert(INSERT, '\n') #Un salto de linea

    for element in tdf: #Un ciclo for para recorrer el arreglo de tdf y mostrar los resultados
        txt.insert(INSERT,element) #Se inserta elemento por elemento en la GUI
        txt.insert(INSERT,'\n') #Salto de linea

    

    plt.figure(1) #Se utiliza el modulo plt para la grafica
    plt.title("Transformada Discreta de Fourier de la muestra ingresada") #Se coloca el titulo de la grafica
    plt.plot(tdfi) #Mandamos el arreglo de la tdf para graficarla
    plt.show() #Se muestra la grafica


def tdfi(): #Funcion para calcular la inversa de la tdf
    muestra = Muestra.get() #Se extrae la muestra de la GUI
    N = eval(muestra) #Se evalua para poder trabajar con ella

    tdfr = [] #Arreglo para almacenar los datos de la transformada(reales)
    tdfi = [] #Arreglo para almacenar los datos de la transformada(Imaginarios)
    tdfii = [] #Arreglo para almacenar los resultados

    for i in range(0 , N): #Un ciclo for para trabajar la formula de la sumatoria
      res = (i)*(e**((1j*2*3.1416*i*i)/N))*(1/N) #La variable res guarda los resultados
      tdfr.append(re(res)) #Se ingresan los datos a su respectivo arreglo
      tdfi.append(im(res)) #Se ingresan los datos a su respectivo arreglo
      tdfii.append(res) #Se ingresan los datos a su respectivo arreglo

  

    txt = scrolledtext.ScrolledText(ventana,width=45,height=15) #Se crea la ventana para mostrar los datos
    txt.grid(column=5,row=30)  #Para la posicion 


    txt.insert(INSERT, "Datos(1 a N-1):") #Se muestra el mensaje

    txt.insert(INSERT, '\n') #Salto de linea

    for element in tdfii: #Con un ciclo for para recorrer todos los resultados
        txt.insert(INSERT,element) #Se insertan en la GUI
        txt.insert(INSERT,'\n') #Salto de linea
 

    plt.figure(1) #Se utiliza el modulo plot para la grafica
    plt.title("Transformada Discreta de Fourier inversa para la muestra ingresada") #Titulo de la grafica
    plt.plot(tdfi) #Se mandan los datos a la grafica
    plt.show() #Se muestra la grafica

def trf(): #Funcion para calcular la transformada rapida de fourier
    muestra = Muestra.get() #Se extraen los datos de la muestra
    N = eval(muestra) #Se evaluan

    trf = [] #Un arreglo para guardar los resultados

    for i in range(0 , N): #Un ciclo for para trabajar la formula de la sumatoria
      res = (i)*math.exp((-2*3.1416*i)/N)**(i-1)*(i-1) #Formula para la trf
      trf.append(res) #Se insertan los resultados en un arreglo

  

    txt = scrolledtext.ScrolledText(ventana,width=45,height=15) #Se crea un espacio para mostrar los datos
    txt.grid(column=5,row=30)  #Para la posicion


    txt.insert(INSERT, "Datos(1 a N-1):") #Se muestra el mensaje

    txt.insert(INSERT, '\n') #Salto de linea

    for element in trf: #Con un ciclo recorremos el arreglo
        txt.insert(INSERT,element) #Se muestra cada elemento
        txt.insert(INSERT,'\n') #Saltod e linea
 
    plt.figure(1) #Utilizamos el modulo plt para graficas
    plt.title("Transformada Rapida de Fourier de la muestra ingresada") #Titulo de la grafica
    plt.plot(trf) #Mandamos los datos para la grafica
    plt.show() #Mostramos la grafica

def trfi(): #Funcion para calcular la inversa de la trf
    muestra = Muestra.get() #Extrameos los datos de la muesta
    N = eval(muestra) #Evaluamos para poder trabajarlos

    trf = [] #Arreglo para almacenar los datos

    for i in range(0 , N): #Con un ciclo for trabajamos la fomrula para la sumatoria
      res = ((i)*math.exp((-2*3.1416*i)/N)**(i-1)*(i-1))*(1/N) #La variable res almacena los resultados
      trf.append(res) #Mandamos los resultados al arreglo

  

    txt = scrolledtext.ScrolledText(ventana,width=45,height=15) #Se crea un espacio para mostrar los resultados
    txt.grid(column=5,row=30)  #Para la posicion



    txt.insert(INSERT, "Datos(1 a N-1):") #Mostramos el mensaje

    txt.insert(INSERT, '\n') #Salto de linea

    for element in trf: #Con un ciclo for recorremos el arreglo
        txt.insert(INSERT,element) #Inseramos cada elemento
        txt.insert(INSERT,'\n') #Salto de linea

   

    plt.figure(1) #Usamos el modulo plt para graficas 
    plt.title("Transformada Rapida de Fourier inversa para la muestra ingresada") #Titulo de la grafica
    plt.plot(trf) #Mandamos los datos para la grafica
    plt.show() #Mostramos la grafica


ventana.mainloop() #Esta funcion reconoce todo lo que estamos haciendo con la ventana y es necesaria para verla