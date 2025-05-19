import tkinter as tk
from tkinter import messagebox

def salir():
    ventana.quit()

def mostrar_acerca_de():
    messagebox.showinfo("Acerca de", "Hola a todos excelente inicio de semana.")

def cambiar_color(color):
    frame_principal.config(bg=color)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Menú")
ventana.geometry("400x300")

# Crear barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Menú "Archivo"
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Menú "Ayuda"
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=mostrar_acerca_de)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Menú "Opciones" con submenú de colores
menu_opciones = tk.Menu(barra_menu, tearoff=0)
submenu_color = tk.Menu(menu_opciones, tearoff=0)
submenu_color.add_command(label="Morado claro", command=lambda: cambiar_color("#f5e0fa"))
submenu_color.add_command(label="Verde claro", command=lambda: cambiar_color("#e8f5e9"))
submenu_color.add_command(label="Azul claro", command=lambda: cambiar_color("#bbdcf9"))
menu_opciones.add_cascade(label="Cambiar color", menu=submenu_color)
barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

# Frame principal que cambiará de color
frame_principal = tk.Frame(ventana, bg="white")
frame_principal.pack(fill="both", expand=True)

# Ejecutar ventana
ventana.mainloop()
