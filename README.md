# imc-calculadora
Se definen las variables que se van a utilizar en el programa
Pedimos los datos del usuario dentro de un bucle while, el ciclo se repetirá hasta que los datos requeridos sean correctos, controlamos la finalización del ciclo con la variable flag.

Dentro del ciclo validamos los datos ingresados utilizando métodos del tipo string
 - isalpha() para validar que el nombre no contenga números o caracteres especiales
 - isdecimal() para validar que los datos edad, estatura y peso sean números

Si son validos realiza un cast en las variables edad, estatura y peso, se asignan a su variable correspondiente
Asignamos True a la variable flag y acaba el ciclo

Calculamos el índice de masa corporal con la formula peso / ((estatura/100)**2)

Asignamos una descripción al valor obtenido de imc dependiendo el rango en que se encuentra

Mostramos los datos ingresados del usuario
