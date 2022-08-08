
#IMPORTACION:
from scipy.io import wavfile  #importamos libreria spicy - sirve para leer archivos en formato ".wav"
import numpy as np       # numpy nos ayudara a realizar operaciones matematicas
import matplotlib.pyplot as plt   # libreria que nos ayudara a realizar los graficos

#FUNCIONES PRINCIPALES:

#Funcion para leer el archivo. Retorna un vector recortado a los 5 segundos y la longitud de dicho vector
def lectura(nombre):
    numero, data1 = wavfile.read('sounds\\'+nombre)  # la funcion "wavfile.read()" reTorna una tutla con un numero y un vector.
    # si dividimos len(data1)/numero obtenemos el tiempo de grabacion (~5.56 s), por lo que reemplazamos
    # el tiempo de grabacion por 5 y obtenemos un nuevo len(data1) que corta al vector en 5 segundos
    longitud = 5*numero         # hallamos la nueva longitud del vector
    data2 = data1[:longitud]   # creamos un nuevo vector recortado en 5 segundos de grabacion
    return data2,longitud    # retornamos la nueva longitud y el nuevo vector en 5 segundos


#Funcion para hallar el nivel de presion sonora con ayuda de una integral numerica (metrodo trapezoidal)
def integral(data2,longitud): # pasamos como parametros el vector y lalongitud del vector
    longitud2 = longitud / 1000   # hallamos n(numero de intervalos)
                                  # lo dividimos entre 1000 para que la complejidad del algoritmo no sea tan alta
    diferencial = 5 / (longitud2)  # hallamos la diferencial de la forma (b-a)/n donde  b= 5 , a =0 , n = longitud2
    suma = 0     # almacenara la sumatoria (diferencial x f1(x) + diferencial x f2(x) .....)
    for i in range(0, len(data2), 1000):  # recorremos el vector para hallar la suma de cada intervalo en el metodo del trapecio
                                          # con un paso de 1000 para que coincida on los n intervalos hallados anteriormente
        suma += diferencial * pow(data2[i], 2) # cada punto del vector se eleva al cuadrado y se multiplica por la diferencial
    presion = 10 * np.log10(1 / 5 * suma)  # utilizando la formula trnsformamos lo obtenido a nivel de presion sonora en decibelios (db)
    return round(presion, 5)  # retornamos el nivel de presion sonora redondeado a 5 decimales



# OPERACIONES Y LLAMADAS A FUNCIONES

# lista que contiene todos los nombre de los archivos de audio
link = ['0.0.wav','0.1.wav','0.2.wav','0.3.wav','0.4.wav',
        '1.0.wav','1.1.wav','1.2.wav','1.3.wav','1.4.wav',
        '2.0.wav','2.1.wav','2.2.wav','2.3.wav','2.4.wav',
        '3.0.wav','3.1.wav','3.2.wav','3.3.wav','3.4.wav',
        '4.0.wav','4.1.wav','4.2.wav','4.3.wav','4.4.wav',
        '5.0.wav','5.1.wav','5.2.wav','5.3.wav','5.4.wav',
        '6.0.wav','6.1.wav','6.2.wav','6.3.wav','6.4.wav',
        '7.0.wav','7.1.wav','7.2.wav','7.3.wav','7.4.wav',
        '8.0.wav','8.1.wav','8.2.wav','8.3.wav','8.4.wav',
        '9.0.wav','9.1.wav','9.2.wav','9.3.wav','9.4.wav',
        '10.0.wav','10.1.wav','10.2.wav','10.3.wav','10.4.wav']



lista = []    #lista donde se almacenara los niveles de presion sonora de cada archivo de audio
for i in range(len(link)):  # recorremos la lista
    data2, longitud = lectura(link[i])   # leemos el archivo con la funcion lectura()
    presion = integral(data2, longitud)  # obtenemos el nivel de presion sonora de cada archivo con la funcion integral()
    lista.append(presion)  # agregamos ese valor a la lista


# Transformacion de lista  matriz
total = [] # lista q alamcenaralas listas
temporal = [] #lista temporal
contador = 0 # contador
for i in range(5,len(lista)+1,5): # recorremos la lista con un paso de 5 y empezando en 5
    temporal = lista[contador:i] # temporal almacenaralos valores desde contadro hasta i-1
                                 # -> primer caso (desde el indice  0 hasta el 4)
    contador+=5   # aumentamos el contador en 5
    total.append(temporal)   #agregamos la lista temporal a la lista total

#NOTA:
# total es una matriz de 11x5 con un total de 55 puntos, los mismo que obtuvimos en la grilla

#GRAFICAMOS:

x = np.linspace(0, 16, 5)  # obtenemos 5 valores entre 0 y 16
y = np.linspace(0, 40, 11)  #obtenemos 11 valores entre 0 y 40
X, Y = np.meshgrid(x, y)    #pasamos a una matriz de 11x5 con los valores entre 0 - 16 y 0 - 40

plt.contourf(X, Y, total,15, cmap='inferno')    # el comando plt.contourf() nos ayudara a graficar el mapa de ruido

plt.imshow(total, extent=[0, 16, 0, 40], origin='lower',  # con el comando imshow() podremos modificar el tamano del grafico
                                                        # y ponerlo a la escal de deseemos
           cmap='inferno')

#LEYENDA

columna = plt.colorbar(orientation = "horizontal", extend = "both",format = "%.0f")   # Con ayuda del comando plt.colorbar
                                # creamos un aleyenda que indicara el color segun aumenta en nivel de presion sonora
columna.set_label("Nivel de presion sonora (db)", size = 8)


plt.title(" MAPA DE RUIDO ",fontsize=10,fontfamily="sans",fontweight="bold",color= 'black')  # titulo del grafico
plt.xlabel("Distancia (m) ",fontsize=8,fontfamily="sans",color= 'black')   # titulo del eje x
plt.ylabel("Distancia (m) ",fontsize=8,fontfamily="sans",color= 'black')   # titulo del eje y


#plt.savefig("Mapa_de_ruido.png")# comando para guardar el grafico en formato png en el mismo directorio de trabajo
plt.show()



