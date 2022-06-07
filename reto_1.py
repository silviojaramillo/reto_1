## Reto de programación 1

""" Crear un programa que solicite al usuario g
una palabra y se evalúe si es par o impar la 
cantidad de letras que la componen. 
De ser impar, de acuerdo a las reglas 
gramaticales del castellano, agregar 
las letras correspondientes.
Finalmente devolver la palabra en dos 
partes iguales o en caso de que después 
de agregar las letras correspondientes 
la palabra no cumpla con los requisitos 
para dividirse en partes iguales 
mostrar un mensaje diciendo que la 
palabra no se puede usar para el reto."""

#Leyendo la palabra que se va a evaluar

text = str(input("Ingrese una palabra: "))
sizeword = len(text)

#Validando si la variable ingresada es de longitud par o impar

if (sizeword % 2 == 0):
    longitud = True
else:
    longitud = False
    
""" De acuerdo a las reglas gramaticales si es terminada en consonante
se agrega es y si termian en vocal solo s """

#volviendo par la longitud de la palabra

if (longitud == False and text[-1] == "a"):
    text = text + "s"
    sizeword += 1
elif (longitud == False and text[-1] == "e"):
    text = text + "s"
    sizeword += 1
elif (longitud == False and text[-1] == "i"):
    text = text + "s"
    sizeword += 1
elif (longitud == False and text[-1] == "o"):
    text = text + "s"
    sizeword += 1
elif (longitud == False and text[-1] == "u"):
    text = text + "s"
    sizeword += 1
elif (longitud == False):
    text = text + "es"
    sizeword +=2
if sizeword % 2 != 0:
    print('La palabra ingresada no cumple con los parámetros necesarios para realizar el reto')
    exit()

#recorriendo la palabra para dividirla en dos partes iguales
newText1 = str()
newText2 = str()
for i in range(sizeword):
    if i <= (sizeword-1)//2:
        newText1 = newText1 + text[i]
    else:
        newText2 = newText2 + text[i]

print('La palabra dividida en partes iguales queda así: ')
print('primera parte: {}'.format(newText1))
print('segunda parte es: {}'.format(newText2))

