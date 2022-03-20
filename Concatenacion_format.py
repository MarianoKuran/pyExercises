#metodo de concatenacion .format()

#opcion 1
nombre = "Mariano"
edad = 22

print("Hola, {}. Tienes {} años.".format(nombre, edad))

#opcion 2

print("Hola, {nombre}. Tienes {edad} años.".format(nombre = "Mariano", edad = 22))

#opcion 3

nombre = "Mariano"
edad = 22

print("Hola, {0}. Tienes {1} años.".format(edad, nombre))
