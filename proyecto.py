
nombre = ""
apellido_paterno = ""
apellido_materno = ""
nombre_completo = ""
edad = None
estatura = None
peso = None
imc = None
imc_descripcion = ""

flag = False

while not flag:

    nombre = input("Ingresa tu nombre: ")
    apellido_paterno = input("Ingresa tu apellido paterno: ")
    apellido_materno = input("Ingresa tu apellido materno: ")
    edad = input("Ingresa tu edad: ")
    estatura = input("Ingresa tu estatura (cm): ")
    peso = input("Ingresa tu peso (kg): ")
 
    if nombre.isalpha() == True and apellido_paterno.isalpha() == True and apellido_materno.isalpha() == True:
        nombre_completo = f'{nombre} {apellido_paterno} {apellido_materno}'.lower().title()
    else: 
        print("Nombre Incorrecto")
        continue

    if edad.isdecimal() == True:
        edad = int(edad)
    else:
        print(f'Edad incorrecta')
        continue

    if estatura.isdecimal() == True:
        estatura = int(estatura)
    else:
        print(f'Estatura incorrecta')
        continue

    if peso.isdecimal() == True:
        peso = int(peso)
    else:
        print(f'Peso incorrecto')
        continue
    
    flag = True

imc = peso / ((estatura/100)**2)

if imc >= 0 and imc <= 15.99 :
        imc_descripcion = "Delgadez severa"
elif imc >= 16.00 and imc <= 16.99 :
        imc_descripcion =  "Delgadez moderada"
elif imc >= 17.00 and imc <= 18.49:
        imc_descripcion =  "Delgadez leve"
elif imc >= 18.50 and imc <= 24.99 :
        imc_descripcion =  "Peso normal"
elif imc >= 25.00 and imc <= 29.99:
        imc_descripcion =  "Sobrepeso"
elif imc >= 30.00 and imc <= 34.99:
        imc_descripcion =  "Obesidad leve"
elif imc >= 35.00 and imc <= 39.00:
        imc_descripcion =  "Obesidad media"
elif imc >= 40.00:
        imc_descripcion =  "Obesidad morbida"


print(f'\nHola {nombre_completo}, estos son tus datos:\n')
print(f'Edad = {edad} años')
print(f'Estatura = {estatura} cm')
print(f'Peso = {peso} kg')
print(f'Imc = {imc:.2f} - {imc_descripcion}')
