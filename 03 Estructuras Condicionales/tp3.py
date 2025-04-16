# #1
# edad=int(input('Ingrese su edad'))
# edadminima=18
# if edad >= edadminima:
#     print('es mayor de edad')
# else:
#     print('es menor')
#

#------------------------

# nota=int(input('Ingrese su nota'))
# notaMinima=6
# if nota >= notaMinima:
#     print('aprobado')
# else:
#     print('desaprobado')

#------------------------

# numero=int(input('Ingrese un numero'))

# if numero % 2 == 0:
#     print('es par')
# else:
#     print('no es par')

#------------------------

# edad=int(input('Ingrese su edad'))
# if edad >=30:
#     print('adulto')
# elif edad >= 18 and edad < 30:
#     print('adulto joven')
# elif edad>= 12 and edad < 18:
#     print('adolescente')
# else:
#     print('niño')

#------------------------

# contraseña=input('ingrese su contraseña')

# longitud=len(contraseña)

# if longitud >=8 and longitud <= 14:
#     print('contraseña correcta')
# else:
#     print('ingrese contraseña correcta')



#------------------------
# from statistics import mode, median, mean 
# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# print(mean(numeros_aleatorios))
# print(median(numeros_aleatorios))
# print(mode(numeros_aleatorios))


#------------------------
# palabra=input('ingrese una palabra')

# if palabra[-1] in 'aeiou':
#     palabraResultante= palabra + '!'
# else:
#     palabraResultante=palabra

# print(palabraResultante)
#------------------------
# opcion=int(input('Ingrese 1 , 2 o 3'))
# nombre=input('ingresa tu nombre ')

# if opcion==1:
#     print(nombre.upper())
# elif opcion==2:
#     print(nombre.lower())
# elif opcion==3:
#     print(nombre.title())
# else:
#     print('ingrese un numero valido')
#------------------------

# magnitud = float(input("Ingrese la magnitud del terremoto: "))


# if magnitud < 3:
#     clasificacion = "Muy leve (imperceptible)"
# elif 3 <= magnitud < 4:
#     clasificacion = "Leve (ligeramente perceptible)"
# elif 4 <= magnitud < 5:
#     clasificacion = "Moderado (sentido por personas, pero generalmente no causa daños)"
# elif 5 <= magnitud < 6:
#     clasificacion = "Fuerte (puede causar daños en estructuras débiles)"
# elif 6 <= magnitud < 7:
#     clasificacion = "Muy Fuerte (puede causar daños significativos)"
# else: 
#     clasificacion = "Extremo (puede causar graves daños a gran escala)"


# print(f"La magnitud del terremoto es: {magnitud}. Categoría: {clasificacion}.")

#------------------------

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("Ingrese el mes del año (1 para enero, 2 para febrero, etc.): "))
dia = int(input("Ingrese el día del mes: "))


if hemisferio == "N": 
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":  # Hemisferio sur
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = None


if estacion:
    print(f"Te encuentras en la estación: {estacion}.")
else:
    print("Hemisferio ingresado no válido. Por favor, ingresa 'N' para norte o 'S' para sur.")
