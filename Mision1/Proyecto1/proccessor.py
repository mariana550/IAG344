import re
# =================================================
# FUNCION 
# Elimina caracter no numericos de una cadena
# cc -> 1.055.754.628 -> 1055754628
# =================================================
def clean_id(value):
    if value is None:
       return ""
    return re.sub(r"\D", "", str(value))
# =================================================
# FUNCION merge_name 
# une nombre y apellido en una sola cadena
# =================================================
def merge_name(name, last_name):
   if name is None:
      name=""
   if last_name is None:
      last_name=""
   return f"{name} {last_name}".strip()
# =================================================
# FUNCION 
# Excel cargar y procesar datos
# =================================================
def process_excel(Path):
   # Acceso a la hoja llamada Datos
   ws = wb["Datos"]
   
