import tkinter as tk
from mipres_tool.handlers.juntas_medicas import ejecutar_descarga_juntas_gui
from mipres_tool.handlers.prescripciones import ejecutar_descarga_prescripcion_gui

def launch_app():
    ventana = tk.Tk()
    ventana.title("MIPRES VIVA1A Manager")
    ventana.geometry("300x200")

    tk.Label(ventana, text="Seleccione una opción", font=("Arial", 14)).pack(pady=20)
    tk.Button(ventana, text="Juntas Médicas", width=25, command=ejecutar_descarga_juntas_gui).pack(pady=10)
    tk.Button(ventana, text="Prescripciones", width=25, command=ejecutar_descarga_prescripcion_gui).pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    launch_app()