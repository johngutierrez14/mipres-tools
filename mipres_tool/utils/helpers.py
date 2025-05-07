from tkinter import filedialog

def tipo_tecnologia(tipo):
    if tipo == 'M':
        return 'Medicamentos'
    elif tipo == 'S':
        return 'Serv. Complementario'
    elif tipo == 'N':
        return 'Nutricionales'
    else:
        return tipo

def dividir_prescripcion(no_prescripcion):
    return {
        "AñoCreacion": no_prescripcion[:4] if len(no_prescripcion) >= 4 else '',
        "MesCreacion": no_prescripcion[4:6] if len(no_prescripcion) >= 6 else '',
        "DiaCreacion": no_prescripcion[6:8] if len(no_prescripcion) >= 8 else '',
        "ConsecutivoID": no_prescripcion[8:] if len(no_prescripcion) > 8 else ''
    }

def formatear_fecha(dateentry):
    return dateentry.get_date().strftime("%Y-%m-%d")

def seleccionar_carpeta(carpeta_var):
    carpeta = filedialog.askdirectory()
    if carpeta:
        carpeta_var.set(carpeta)