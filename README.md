PAV - P3: estimación de pitch
=============================

Esta práctica se distribuye a través del repositorio GitHub [Práctica 3](https://github.com/albino-pav/P3).
Siga las instrucciones de la [Práctica 2](https://github.com/albino-pav/P2) para realizar un `fork` de la
misma y distribuir copias locales (*clones*) del mismo a los distintos integrantes del grupo de prácticas.

Recuerde realizar el *pull request* al repositorio original una vez completada la práctica.

Ejercicios básicos
------------------

- Complete el código de los ficheros necesarios para realizar la estimación de pitch usando el programa
  `get_pitch`.

   * Complete el cálculo de la autocorrelación e inserte a continuación el código correspondiente.
> Mostramos a continuación el código de cálculo de la autocorrelación:
> 
> ![image](https://user-images.githubusercontent.com/125367047/236632472-3c1a4d5a-b74b-4132-8358-eafd174d7e22.png)

   * Inserte una gŕafica donde, en un *subplot*, se vea con claridad la señal temporal de un segmento de
     unos 30 ms de un fonema sonoro y su periodo de pitch; y, en otro *subplot*, se vea con claridad la
	 autocorrelación de la señal y la posición del primer máximo secundario.

	 NOTA: es más que probable que tenga que usar Python, Octave/MATLAB u otro programa semejante para
	 hacerlo. Se valorará la utilización de la biblioteca matplotlib de Python.
> Haciendo zoom de la señal de prueba.wav sobre los primeros 30 ms (donde se percibe la vocal 'a') encontramos los siguientes resultados para la autocorrelación de la señal, destacando la visualización del primer máximo secundario sobre la muestra #380 aproximadamente:
> 
> ![image](https://user-images.githubusercontent.com/125367047/236637056-2f0bc3be-bd01-4faa-86b6-692cbb8e849b.png)

   * Determine el mejor candidato para el periodo de pitch localizando el primer máximo secundario de la
     autocorrelación. Inserte a continuación el código correspondiente.
> Localizado el primer máximo secundario anteriormente, añadimos el código correspondiente:
> 
> <img width="443" alt="image" src="https://user-images.githubusercontent.com/125367047/236637965-29ce3aea-3416-483b-9feb-b04b6e5c4f1d.png">

   * Implemente la regla de decisión sonoro o sordo e inserte el código correspondiente.

   * Puede serle útil seguir las instrucciones contenidas en el documento adjunto `código.pdf`.
> Determinamos el tono en base a unos umbrales de decisión, donde en función de si la autocorrelación y la potencia se encuentran dentro o fuera del rango, definiremos que hay silencio o voz.
> 
> <img width="596" alt="image" src="https://user-images.githubusercontent.com/125367047/236673454-17d1f37c-11d3-4a75-bb40-f8f6c6a12aa4.png">


- Una vez completados los puntos anteriores, dispondrá de una primera versión del estimador de pitch. El 
  resto del trabajo consiste, básicamente, en obtener las mejores prestaciones posibles con él.

  * Utilice el programa `wavesurfer` para analizar las condiciones apropiadas para determinar si un
    segmento es sonoro o sordo. 
	
	  - Inserte una gráfica con la estimación de pitch incorporada a `wavesurfer` y, junto a ella, los 
	    principales candidatos para determinar la sonoridad de la voz: el nivel de potencia de la señal
		(r[0]), la autocorrelación normalizada de uno (r1norm = r[1] / r[0]) y el valor de la
		autocorrelación en su máximo secundario (rmaxnorm = r[lag] / r[0]).

		Puede considerar, también, la conveniencia de usar la tasa de cruces por cero.

	    Recuerde configurar los paneles de datos para que el desplazamiento de ventana sea el adecuado, que
		en esta práctica es de 15 ms.
> Empleamos la función cout que permite mostrar por consola la información de la potencia, la autorrelación en 1 y la autocorrelación del pitch, para cada una de las tramas.
> 
> <img width="451" alt="image" src="https://user-images.githubusercontent.com/125367047/236668716-e2ab8445-d3a7-4bb4-8e02-9973bc76c22d.png">
> 
> 
> A continuacion, escribimos distintos ficheros .out para más adelante, poder observar las funciones r(lag)/r(0) y r(1)/r(0) mediante wavesurfer. Utilizamos cut para quedarnos con las columnas que nos interesan para cada caso:
> 
> <img width="602" alt="image" src="https://user-images.githubusercontent.com/125367047/236669298-6aadaa86-7204-468d-b1e4-656a0c1b743d.png">
> 
> 
> Los diferentes subplots representados son (de arriba abajo) rmaxnorm, r1norm, pot_r, y finalmente la señal que hemos utilizado prueba.wav.
> 
> ![image](https://user-images.githubusercontent.com/125367047/236670271-16c3582d-3166-4a22-81b6-1957fc9b3c47.png)
> 
> Obervamos que donde tenemos segmentos de voz (sonoros), ambas autocorrelaciones tienen un valor cercano a 1. Esto se debe a que las muestras cercanas de las tramas de voz son parecidas entre ellas. A partir de estas gráficas encontramos los valores iniciales para nuestros umbrales, que modificaremos más adelante al optimizar los parametros de detección de pitch.



	- Use el estimador de pitch implementado en el programa `wavesurfer` en una señal de prueba y compare
	    su resultado con el obtenido por la mejor versión de su propio sistema.  Inserte una gráfica
		ilustrativa del resultado de ambos estimadores.
     
		Aunque puede usar el propio Wavesurfer para obtener la representación, se valorará
	 	el uso de alternativas de mayor calidad (particularmente Python).
> A continuación vemos la estimación de pitch que realiza wavesurfer, además de la señal utilizada prueba.wav.
> 
> ![image](https://user-images.githubusercontent.com/125367047/236671544-52412e17-e152-44ea-ad1a-81a5dc871071.png)

  * Optimice los parámetros de su sistema de estimación de pitch e inserte una tabla con las tasas de error
    y el *score* TOTAL proporcionados por `pitch_evaluate` en la evaluación de la base de datos 
	`pitch_db/train`..
> Con los valores de threshold ya "maximizados" nuestro sistema de decisión tendrá un acierto del 89.57%, resultado previo a aplicar cualquier tipo de pre/postprocesado.
> 
> <img width="378" alt="image" src="https://user-images.githubusercontent.com/125367047/236673291-acce316d-593a-4f1a-89ec-d8b24fbb3002.png">

Ejercicios de ampliación
------------------------

- Usando la librería `docopt_cpp`, modifique el fichero `get_pitch.cpp` para incorporar los parámetros del
  estimador a los argumentos de la línea de comandos.
  
  Esta técnica le resultará especialmente útil para optimizar los parámetros del estimador. Recuerde que
  una parte importante de la evaluación recaerá en el resultado obtenido en la estimación de pitch en la
  base de datos.

  * Inserte un *pantallazo* en el que se vea el mensaje de ayuda del programa y un ejemplo de utilización
    con los argumentos añadidos.
> A continuación mostramos los argumentos añadidos con sus valores por default:
> 
> <img width="602" alt="image" src="https://user-images.githubusercontent.com/125367047/236673215-0b69632b-8516-42dc-acd2-22d8c0d45730.png">

- Implemente las técnicas que considere oportunas para optimizar las prestaciones del sistema de estimación
  de pitch.

  Entre las posibles mejoras, puede escoger una o más de las siguientes:

  * Técnicas de preprocesado: filtrado paso bajo, diezmado, *center clipping*, etc.
  * Técnicas de postprocesado: filtro de mediana, *dynamic time warping*, etc.
  * Métodos alternativos a la autocorrelación: procesado cepstral, *average magnitude difference function*
    (AMDF), etc.
  * Optimización **demostrable** de los parámetros que gobiernan el estimador, en concreto, de los que
    gobiernan la decisión sonoro/sordo.
  * Cualquier otra técnica que se le pueda ocurrir o encuentre en la literatura.

  Encontrará más información acerca de estas técnicas en las [Transparencias del Curso](https://atenea.upc.edu/pluginfile.php/2908770/mod_resource/content/3/2b_PS%20Techniques.pdf)
  y en [Spoken Language Processing](https://discovery.upc.edu/iii/encore/record/C__Rb1233593?lang=cat).
  También encontrará más información en los anexos del enunciado de esta práctica.

  Incluya, a continuación, una explicación de las técnicas incorporadas al estimador. Se valorará la
  inclusión de gráficas, tablas, código o cualquier otra cosa que ayude a comprender el trabajo realizado.

  También se valorará la realización de un estudio de los parámetros involucrados. Por ejemplo, si se opta
  por implementar el filtro de mediana, se valorará el análisis de los resultados obtenidos en función de
  la longitud del filtro.
> En nuestro caso, hemos aplicado una técnica de center-clipping a nivel de preprocesado y posteriormente un filtro de mediana.
> Al implementar center-clipping, definimos un nuevo umbral que hemos ajustado a un valor óptimo de 0.0005. Con esta técnica eliminamos o ponemos a zero todos los valores de los instantes de tiempo que hemos detectado como silencio, con esto lo que estamos consiguiendo es una señal robusta ante la presencia de ruido. El código implementado queda de la siguiente forma:
> 
> <img width="473" alt="image" src="https://user-images.githubusercontent.com/125367047/236673709-dc1bfa2b-ded7-45c6-8b3b-e7bb03c71b1c.png">
> 
> La segunda técnica aplicada se trata de un filtro de mediana, donde cogemos el entorno de cada una de las muestras (en nuestro caso únicamente la muestra anterior y la muestra posterior al tener una longitud = 3) y comprobamos cual es su valor medio.
> 
> <img width="525" alt="image" src="https://user-images.githubusercontent.com/125367047/236674953-e0cf66ca-acdf-49a1-a107-48207ac0236a.png">
> 
> Tras haber aplicado las anteriores mejoras comentadas, obtenemos un resultado final de 90.22% de acierto.
> 
> <img width="369" alt="image" src="https://user-images.githubusercontent.com/125367047/236675399-87a9f4b8-9aed-4979-a454-83e33e1ceb65.png">



   

Evaluación *ciega* del estimador
-------------------------------

Antes de realizar el *pull request* debe asegurarse de que su repositorio contiene los ficheros necesarios
para compilar los programas correctamente ejecutando `make release`.

Con los ejecutables construidos de esta manera, los profesores de la asignatura procederán a evaluar el
estimador con la parte de test de la base de datos (desconocida para los alumnos). Una parte importante de
la nota de la práctica recaerá en el resultado de esta evaluación.
