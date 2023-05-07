import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np


#Leemos el fichero de audio
audio, fm = sf.read("prueba30ms.wav")

#Eje de tiempo
time = (np.linspace(0, len(audio)-1, len(audio)))/fm 

#Calculo de autocorrelación
r = np.correlate(audio, audio, "same")
r = r / r[int(len(r)/2)] 
raxis = np.arange(len(r))

#Representamos las gráficas
plt.subplot(2,1,1)
plt.plot(time, audio)
plt.grid(True)
plt.xlabel("Tiempo(s)")
plt.ylabel("Amplitud")

plt.subplot(2,1,2)
plt.plot(raxis, r)
plt.grid(True)
plt.xlabel("Muestras")
plt.ylabel("Autocorrelación")

plt.show()