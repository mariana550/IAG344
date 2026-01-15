#LIBBRERIAS
import re
""""
Exprexiones regulares en PYTHON
Problemas reales
"""
#CODIGO
print("libreria cargada correctamente")

#Ejemplo 1
texto ="Mi  numero es 23456789"
resultado = re.search(r"\d+",texto)
print(f"{texto} Resultado {resultado.group()}")

texto ="Mi  numero es 98765432"
resultado = re.search(r"\d+",texto)
print(f"{texto} Resultado {resultado.group()}")