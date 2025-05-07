import os
import requests
from tkinter import messagebox, Toplevel, Label, Entry, Button, StringVar
from tkcalendar import DateEntry
from mipres_tool.utils.helpers import seleccionar_carpeta, formatear_fecha
from mipres_tool.utils.procesar_juntas_medicas import procesar_juntas_medicas
from mipres_tool.config import API_URL_JUNTA_MEDICA, TOKEN, NIT

def ejecutar_descarga_juntas_gui():
    def ejecutar():
        fecha = formatear_fecha(fecha_entry)
        carpeta = carpeta_var.get()
        if not carpeta:
            messagebox.showwarning("Carpeta requerida", "Seleccione carpeta de destino.")
            return

        nombre_archivo = f"{fecha.replace('-', '')}_JM.json"
        url = f"{API_URL_JUNTA_MEDICA}/{NIT}/{TOKEN}/{fecha}"

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

            excel = procesar_juntas_medicas(carpeta)
            if excel:
                messagebox.showinfo("Éxito", f"Archivo generado en:\n{excel}")
            else:
                messagebox.showwarning("Procesamiento", "No se pudo procesar el archivo.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    ventana = Toplevel()
    ventana.title("Descargar Juntas Médicas")
    ventana.geometry("400x300")

    Label(ventana, text="Fecha:").pack(pady=5)
    fecha_entry = DateEntry(ventana, width=20, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
    fecha_entry.pack(pady=5)

    Label(ventana, text="Carpeta de destino:").pack(pady=5)
    carpeta_var = StringVar()
    Entry(ventana, textvariable=carpeta_var, width=35).pack(pady=5)
    Button(ventana, text="Buscar carpeta", command=lambda: seleccionar_carpeta(carpeta_var)).pack(pady=5)

    Button(ventana, text="Descargar y procesar", command=ejecutar).pack(pady=20)