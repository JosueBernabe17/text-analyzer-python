texto = input("ingresar un texto a su eleccion: ")
letras = []
texto = texto.lower()
letras.append(input("ingresar la primera letra: ").lower())
letras.append(input("ingresar la segunda letra: ").lower())
letras.append(input("ingresar la tercera letra: ").lower())
print("\n")
print("CANTIDAD DE LETRAS")
print("\n")

cantidad_de_letras1 = texto.count(letras[0])
cantidad_de_letras2 = texto.count(letras[1])
cantidad_de_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} repetida {cantidad_de_letras1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetida {cantidad_de_letras2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetida {cantidad_de_letras3} veces")
print("\n")
print("CANTIDAD DE PALABRAS")
print("\n")
palabra = texto.split()
print(f"Hemos encontrado {len(palabra)} palabras en tu texto")

print("LETRAS DE INICO Y FIN")
print("\n")
letras_inicio = texto[0]
letras_fin = texto[-1]
print(f"la letra inicial es {letras_inicio} y la letra final es {letras_fin}")

print("TEXTO INVERTIDO")
print("\n")
palabra.reverse()
texto_invertido = ' '.join(palabra)
print(f"SI ORDENAMOS TU TEXTO AL REVES VA A DECIR: '{texto_invertido}' ")

print("\n")
print("buscando la palabra python")
buscar_palabra = 'python' in texto
print(bool(buscar_palabra))
print(f"la palabra python se encuentra en  el texto : {buscar_palabra}")

