# ui.py
# Capa de interfaz gráfica (Tkinter)
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from controller import procesar_instruccion

def iniciar_app():
    # Ventana principal
    root = tk.Tk()
    root.title("Procesador Excel con IA")
    root.geometry("500x300")

    # Etiqueta
    tk.Label(root, text="Escriba una instrucción en lenguaje natural").pack(pady=10)

    def seleccionar_excel():
        return filedialog.askopenfilename(
        title="Seleccionar archivo Excel",
        filetypes=[("Archivo Excel","*.xlsx")]
        )
    def on_clic_procesar():
        path = seleccionar_excel()
        if path:
            path_label.config(text=path)
    
    boton = tk.Button(
        root,
        text="Seleccionar archivo Excel",
        command=on_clic_procesar,
        width=30,
        height=2
    )
    boton.pack(pady=15)
    # ETIQUETA
    path_label = tk.Label(root, 
                         text="Sin archivo seleccionado",
                         width=30,
                         height=2
                         )
    path_label.pack(pady=10)

    # Campo de texto
    entrada = tk.Entry(root, width=60)
    entrada.pack(pady=5)

    # Acción del botón
    def ejecutar():
        texto = entrada.get()
        path = path_label.cget("text")
        exito, mensaje = procesar_instruccion(texto,path)

        if exito:
            messagebox.showinfo("Resultado", mensaje)
        else:
            messagebox.showerror("Error", mensaje)

    # Botón
    tk.Button(root, text="Ejecutar instrucción", command=ejecutar).pack(pady=20)
    root.mainloop()