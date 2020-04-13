######### Taller 2 ##########

# calificaciones
# calif = {
#     "calculo":0, 
#     "fisica":0,
#     "astronomia":0,
#     }
# calif["calculo"] = float(input("Escriba la nota de calculo: "))
# calif["fisica"] = float(input("Escriba la nota de fisica: "))
# calif["astronomia"] = float(input("Escriba la nota de astronomia: "))

# prom= float((calif["calculo"]+calif["fisica"]+calif["astronomia"])/3)
# print("El promedio es: " +str(prom))

# #Mejor nota
# if calif["calculo"] > calif["fisica"] > calif["astronomia"]:
#     print("La materia con mejor nota es calculo")
# elif calif["fisica"] > calif["astronomia"] > calif["calculo"]:
#     print("La materia con mejor nota es fisica")
# elif calif["astronomia"] > calif["fisica"] > calif["calculo"]:
#     print("La materia con mejor nota es astronomia")

# #Promedio, suma, mayor y menor
# numeros = []
# def mayor_menor(numeros):
#     mayor = numeros[0]
#     menor = numeros[0]

#     for numero in numeros:
#         if numero > mayor:
#             mayor = numero
#         elif numero < menor:
#             menor = numero

#     print("Mayor:", mayor)
#     print("Menor:", menor)

# def promedio(numeros):
#     acum =0
#     for i in numeros:
#         acum=int(acum+numeros[i])
#         print ("Promedio: "+str(acum/len(numeros)))
#         print ("Suma de los numeros: "+str(acum))

# for i in range(10):
#   numero = int(input("Introduce el número {}: ".format(i + 1)))
#   numeros.append(numero)

# promedio(numeros)
# mayor_menor(numeros)


#Palindromo
# igual, aux = 0, 0
# texto = input("Ingrese la palabra que desea evaluar: ")

# for i in reversed(range(0, len(texto))):
#   if texto[i].lower() == texto[aux].lower():
#     igual += 1
#   aux += 1
# if len(texto) == igual:
#   print("es palindromo")
# else:
#     print("no es palindromo")

# #Frecuencia de las palabras
# cadenaPalabras = str(input("Escriba su parrafo a leer: "))
# listaPalabras = cadenaPalabras.split()

# frecuenciaPalab = []
# for w in listaPalabras:
#     frecuenciaPalab.append(listaPalabras.count(w))

# print("Frecuencia de las palabras\n" + str(list(zip(listaPalabras, frecuenciaPalab))))

#Contar vocales
# cad = str(input("Escriba la palabra con vocales: "))
# voc = 0
# for c in cad:
#     if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
#         voc=voc+1
# print ("Numero de vocales: "+ str(voc))

#Frecuencia de vocales de una frase
# frecuenciaPalab = []
# voc = 0

# cad = str(input("Escriba el parrafo con vocales: "))
# listaPalabras = cad.split()

# for c in listaPalabras:
    
#     if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
#         voc=voc+1
#         frecuenciaPalab.append(listaPalabras.count(c))

# print ("Numero de vocales: "+ str(voc))
# print("Frecuencia de las vocales\n" + str(list(zip(listaPalabras, frecuenciaPalab))))

#Eliminar vocales de palabra
# vocales = ['a','A','e','E','i','I','o','O','u','U']
# res = ''

# cad = str(input("Escriba la palabra con vocales: "))
# for letra in cad:
#     if letra not in vocales:
#         res += letra
# print ("Su palabra sin vocales es: "+ str(res))

#Pares
# par = []

# for i in range(0,100):
#     if (i % 2 == 0):
#         par.append(i)

# print("Los números pares son : " + str(par))
