import tkinter as tk
from tkinter import ttk

# Función para procesar los datos
def procesar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    
    if not nombre or not edad:
        label_resultado.config(text="Por favor, completa todos los campos.", foreground="red")
        return
    
    try:
        edad = int(edad)
        mensaje = f"Nombre: {nombre}\nEdad en 5 años: {edad + 5}"
        label_resultado.config(text=mensaje, foreground="green")
    except ValueError:
        label_resultado.config(text="Edad debe ser un número.", foreground="red")

# Ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Notebook")
ventana.geometry("400x300")

# Notebook (pestañas)
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand=True)

# --------- PESTAÑA 1: Ingreso de datos ----------
tab_ingreso = ttk.Frame(notebook)
notebook.add(tab_ingreso, text="Ingreso de Datos")

# Frame para entradas
frame_entradas = tk.Frame(tab_ingreso, bg="#003976")
frame_entradas.pack(pady=10, padx=10, fill='both', expand=True)

tk.Label(frame_entradas, text="Nombre:").grid(row=0, column=0, sticky='e')
entry_nombre = tk.Entry(frame_entradas)
entry_nombre.grid(row=0, column=1)

tk.Label(frame_entradas, text="Edad:").grid(row=1, column=0, sticky='e')
entry_edad = tk.Entry(frame_entradas)
entry_edad.grid(row=1, column=1)

# Frame para botones
frame_botones = tk.Frame(tab_ingreso, bg="#00409f")
frame_botones.pack(pady=10)

btn_procesar = tk.Button(frame_botones, text="Procesar", command=procesar_datos)
btn_procesar.pack()

# --------- PESTAÑA 2: Resultados ----------
tab_resultado = ttk.Frame(notebook)
notebook.add(tab_resultado, text="Resultados")

label_resultado = tk.Label(tab_resultado, text="Aquí aparecerán los resultados.", bg="#A1FAB9", fg="black", font=("Arial", 12), justify="left")
label_resultado.pack(padx=20, pady=20, anchor="w", fill='both', expand=True)

# Ejecutar ventana
ventana.mainloop()
