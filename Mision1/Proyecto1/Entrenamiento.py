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

#Ejemplo 2
texto ="Mi  numero es 98765432"
resultado = re.findall(r"\d+",texto)
print(f"{texto} Resultado {resultado}")

texto ="Mi  numero es 789654-56"
resultado = re.findall(r"\d+",texto)
print(f"{texto} Resultado {resultado}")

documento1 = "cc.1.055.754.628"

def clean_id(documento):
    return re.sub(r"\D","",documento)
print(clean_id(documento1))
