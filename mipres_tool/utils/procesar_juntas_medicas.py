import os
import json
import pandas as pd
from mipres_tool.utils.helpers import dividir_prescripcion, tipo_tecnologia

def procesar_juntas_medicas(folder_path):
    juntasMedicas_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    contenido_json = json.load(f)
                    for item in contenido_json:
                        junta_medica = item.get('junta_profesional', {})

                        no_prescripcion = junta_medica.get('NoPrescripcion', '')
                        prescripcion_dividida = dividir_prescripcion(no_prescripcion)
                        entidadJuntaMedica = junta_medica.get('CodEntJM', '')
                        EPS = entidadJuntaMedica[:3] if len(entidadJuntaMedica) >= 3 else ''

                        juntasMedicas_data.append({
                            'No Prescripcion': no_prescripcion,
                            'Fecha prescripcion': junta_medica.get('FPrescripcion'),
                            'Fecha creacion': f"{prescripcion_dividida['AñoCreacion']}-{prescripcion_dividida['MesCreacion']}-{prescripcion_dividida['DiaCreacion']}",
                            'Tipo de Tecnologia': tipo_tecnologia(junta_medica.get('TipoTecnologia', '')),
                            'Estado junta medica': junta_medica.get('EstJM', ''),
                            'Justificacion Tecnica': junta_medica.get('JustificacionTecnica', ''),
                            'No Acta': junta_medica.get('NoActa', ''),
                            'Fecha Proceso': junta_medica.get('FProceso', ''),
                            'EPS': EPS,
                        })
                except Exception as e:
                    print(f"Error al procesar {filename}: {e}")

    if juntasMedicas_data:
        df = pd.DataFrame(juntasMedicas_data)
        output_file = os.path.join(folder_path, "junta_medica.xlsx")
        df.to_excel(output_file, index=False)
        return output_file
    return None
