
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

def lectura(nombre):
    numero, data1 = wavfile.read(nombre)


    longitud = 5*numero
    data2 = data1[:longitud]
    return data2,longitud



def integral(data2,longitud):
    longitud2 = longitud / 1000

    diferencial = 5 / (longitud2)
    suma = 0
    for i in range(0, len(data2), 1000):
        suma += diferencial * pow(data2[i], 2)
    presion = 10 * np.log10(1 / 5 * suma)
    return round(presion, 5)




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



lista = []
for i in range(len(link)):
    data2, longitud = lectura(link[i])
    presion = integral(data2, longitud)
    lista.append(presion)



total = []
temporal = []
contador = 0
for i in range(5,len(lista)+1,5):
    temporal = lista[contador:i]
    contador+=5
    total.append(temporal)



x = np.linspace(0, 16, 5)
y = np.linspace(0, 40, 11)
X, Y = np.meshgrid(x, y)

plt.contourf(X, Y, total,15, cmap='inferno')

plt.imshow(total, extent=[0, 16, 0, 40], origin='lower',
           cmap='inferno')

#LEYENDA

columna = plt.colorbar(orientation = "horizontal", extend = "both",format = "%.0f")

columna.set_label("Nivel de presion sonora (db)", size = 8)


plt.title(" MAPA DE RUIDO ",fontsize=10,fontfamily="sans",fontweight="bold",color= 'black')
plt.xlabel("Distancia (m) ",fontsize=8,fontfamily="sans",color= 'black')
plt.ylabel("Distancia (m) ",fontsize=8,fontfamily="sans",color= 'black')


plt.show()







