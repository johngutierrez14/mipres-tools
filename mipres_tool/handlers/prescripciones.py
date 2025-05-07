import os
import requests
from tkinter import messagebox, Toplevel, Label, Entry, Button, StringVar
from tkcalendar import DateEntry

from mipres_tool.utils.helpers import seleccionar_carpeta, formatear_fecha
from mipres_tool.utils.procesar_prescripcion import procesar_prescripciones
from mipres_tool.config import API_URL_PRESCRIPCION, TOKEN, NIT

def ejecutar_descarga_prescripcion_gui():
    def ejecutar_descarga_prescripcion():
        fecha = formatear_fecha(fecha_entry)
        carpeta = carpeta_var.get()
        if not carpeta:
            messagebox.showwarning("Carpeta requerida", "Seleccione carpeta de destino.")
            return
        
        nombre_archivo = f"{fecha.replace('-', '')}_PRES.json"
        url = f"{API_URL_PRESCRIPCION}/{NIT}/{fecha}/{TOKEN}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            
            if not response.text or response.text.strip() == "[]":
                messagebox.showwarning("Sin datos", "No se encontraron datos.")
                return

            os.makedirs(carpeta, exist_ok=True)
            path = os.path.join(carpeta, nombre_archivo)
            with open(path, "w", encoding="utf-8") as f:
                f.write(response.text)

            excel = procesar_prescripciones(carpeta)
            if excel:
                messagebox.showinfo("Éxito", f"Archivo generado en:\n{excel}")
            else:
                messagebox.showwarning("Procesamiento", "No se pudo procesar el archivo.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    ventana_descarga = Toplevel()
    ventana_descarga.title("Descargar prescripciones del día")
    ventana_descarga.geometry("400x350")

    Label(ventana_descarga, text="Seleccione una fecha:").pack(pady=(10, 0))
    fecha_entry = DateEntry(ventana_descarga, width=20, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
    fecha_entry.pack(pady=5)

    Label(ventana_descarga, text="Seleccione carpeta de destino:").pack(pady=(10, 0))
    carpeta_var = StringVar()
    Entry(ventana_descarga, textvariable=carpeta_var, width=35).pack(pady=2)
    Button(ventana_descarga, text="Buscar carpeta", command=lambda: seleccionar_carpeta(carpeta_var)).pack(pady=5)

    Button(ventana_descarga, text="Descargar y procesar", command=ejecutar_descarga_prescripcion).pack(pady=30)  