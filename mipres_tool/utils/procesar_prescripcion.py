import os
import json
import pandas as pd

def procesar_prescripciones(folder_path):
    prescripcion_data = []
    # Conjunto para garantizar valores únicos en 'Consecutivo ID'
    consecutivo_ids_unicos = set()
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    contenido_json = json.load(f)
                    for item in contenido_json:
                        prescripcion = item.get('prescripcion', {})
                        # Divide 'NoPrescripcion' en partes
                        no_prescripcion = prescripcion.get('NoPrescripcion', '')
                        AñoCreacion = no_prescripcion[:4]  # Los primeros 4 caracteres
                        MesCreacion = no_prescripcion[4:6]  # Los siguientes 2 caracteres
                        DiaCreacion = no_prescripcion[6:8]  # Los siguientes 2 caracteres
                        ConsecutivoID = no_prescripcion[8:]  # Los caracteres restantes
                        
                        # Verificar si el 'Consecutivo ID' ya existe
                        if ConsecutivoID not in consecutivo_ids_unicos:
                            consecutivo_ids_unicos.add(ConsecutivoID)  # Agregar al conjunto
                        
                        prescripcion_data.append({
                            'No Prescripcion': no_prescripcion,
                            'Fecha creacion': f"{AñoCreacion}-{MesCreacion}-{DiaCreacion}",
                            'Fecha Prescripcion': prescripcion.get('FPrescripcion', ''),
                            'Hora Prescripcion': prescripcion.get('HPrescripcion', ''),
                            'CodHabIPS': prescripcion.get('CodHabIPS', ''),
                            'Identificacion Profesional': prescripcion.get('TipoIDProf', '') + ' ' + prescripcion.get('NumIDProf', ''),
                            'Nombre Profesional': prescripcion.get('PNProfS', '') + ' ' + prescripcion.get('PAProfS', '') + ' ' + prescripcion.get('SAProfS', ''),
                            'Identificacion Paciente': prescripcion.get('TipoIDPaciente', '') + ' ' + prescripcion.get('NroIDPaciente', ''),
                            'Nombre Paciente': prescripcion.get('PNPaciente', '') + ' ' + prescripcion.get('PAPaciente', '') + ' ' + prescripcion.get('SAPaciente', ''),
                            'Codigo ambito de Atencion': prescripcion.get('CodAmbAte', ''),
                            'Prestación se trata de referencia o contrareferencia': prescripcion.get('RefAmbAte', ''),
                            'Tiene un caso sospechoso o confirmado de COVID19': prescripcion.get('PacCovid19', ''),
                            'Tiene Enfermedad Huérfana': prescripcion.get('EnfHuerfana', ''),
                            'Código Enfermedad Huérfana': prescripcion.get('CodEnfHuerfana', ''),
                            'La enfermedad huérfana es el diagnóstico principal': prescripcion.get('EnfHuerfanaDX', ''),
                            'Codigo Diagnostico Principal': prescripcion.get('CodDxPpal', ''),
                            'Código Diagnóstico Relacionado 1': prescripcion.get('CodDxRel1', ''),
                            'Código Diagnóstico Relacionado 2': prescripcion.get('CodDxRel2', ''),
                            'Requiere soporte nutricional': prescripcion.get('SopNutricional', ''),
                            'Codigo de la EPS': prescripcion.get('CodEPS', ''),
                            'Estado Prescripcion': prescripcion.get('EstPres', ''),
                        })
                except Exception as e:
                    print(f"Error al procesar {filename}: {e}")

    if prescripcion_data:
        df = pd.DataFrame(prescripcion_data)
        
        # Elimina filas completamente vacías
        df = df.dropna(subset=['No Prescripcion'])
        df = df[df['No Prescripcion'].str.strip() != '']
        df = df.dropna(how='all')
        
        output_file = os.path.join(folder_path, "Prescripciones Actuales.xlsx")
        df.to_excel(output_file, index=False)
        return output_file
    return None