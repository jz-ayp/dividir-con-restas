"""
Dividir con restas.
"""

# Entradas
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

# Proceso
cociente = 0
residuo = dividendo
while residuo >= divisor:
    residuo -= divisor
    cociente += 1

# Salidas
print("Cociente:", cociente)
print("Residuo:", residuo)
