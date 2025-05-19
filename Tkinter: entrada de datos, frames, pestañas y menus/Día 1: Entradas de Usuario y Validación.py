import tkinter as tk
from tkinter import messagebox

def validar_datos():
    temp_celsius = entrada_temp.get()
    humedad = entrada_humedad.get()

    if not temp_celsius.strip() or not humedad.strip():
        label_resultado.config(text="❌ Datos no válidos: campos vacíos", fg="red")
        return

    try:
        temp_c = float(temp_celsius)
        humedad_val = float(humedad)
        temp_f = (temp_c * 9/5) + 32
        label_resultado.config(
            text=f"✅ Datos válidos\nTemperatura: {temp_c:.1f}°C = {temp_f:.1f}°F\nHumedad: {humedad_val:.1f}%", fg="green"
        )
    except ValueError:
        label_resultado.config(text="❌ Datos no válidos: ingresa números", fg="red")

# Crear ventana
ventana = tk.Tk()
ventana.title("Validador de Datos")
ventana.geometry("300x200")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Temperatura (°C):").pack()
entrada_temp = tk.Entry(ventana)
entrada_temp.pack()

tk.Label(ventana, text="Humedad (%):").pack()
entrada_humedad = tk.Entry(ventana)
entrada_humedad.pack()

# Botón de validación
boton_validar = tk.Button(ventana, text="Validar Datos", command=validar_datos)
boton_validar.pack(pady=10)

# Etiqueta de resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

# Ejecutar ventana
ventana.mainloop()
