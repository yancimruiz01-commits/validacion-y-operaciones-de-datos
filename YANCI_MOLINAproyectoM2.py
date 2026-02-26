#1. LONGITUD DE UNA FRASE
#  Solicitar al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")

longitud = len(palabra)

# Validar la longitud según los criterios
if 4 <= longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras")
else:  # longitud > 8
     print(f"Sobran letras. Tiene {longitud} letras")


#2.ENCUENTRA EL CUADRANTE
    # Solicita las coordenadas al usuario
x = int(input("Ingrese X: "))
y = int(input("Ingrese Y: "))

# Verifica que ninguna coordenada sea 0
if x == 0 or y == 0:
    print("Error: Las coordenadas no pueden ser 0.")
else:
    # Identifica el cuadrante
    if x > 0 and y > 0:
        cuadrante = "I"
    elif x < 0 and y > 0:
        cuadrante = "II"
    elif x < 0 and y < 0:
        cuadrante = "III"
    else:  # x > 0 and y < 0
        cuadrante = "IV"
    
    print(f"El punto se encuentra en el cuadrante {cuadrante}")
    print(f"(X,Y): ({x},{y})")
