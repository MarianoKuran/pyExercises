#concatenacion con metodo f-Strings

print("Aplicando f-Strings")

nombre = "Mariano"
edad = 22

f"Hola, {nombre}. Tienes {edad} años."

#Ejemplo 2

print(f"El resultado de 4+1 es: {4+1}")

#Ejemplo 3
nombre = "Mariano"
estatura = 1.60
edad = 22

print(f"Hola, {nombre}. Tienes {edad} años y tu estatura es {estatura} metros.")

#Ejemplo 4

nombre = input("¿cual es tu nombre?: ")
num_1 = int(input("Ingresa un numero: "))
num_2 = int(input("Ingresa un numero: "))

print(f"Hola, {nombre}. El resultado de {num_1} + {num_2} es: {num_1 + num_2}.")
