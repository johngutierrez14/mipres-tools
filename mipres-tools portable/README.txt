# mipres-tools-USB

Esta herramienta permite descargar, procesar y exportar archivos JSON de prescripciones y juntas médicas del sistema MIPRES, convirtiéndolos en archivos Excel de manera rápida y eficiente.

## Requisitos previos

- Sistema operativo: Windows
- Tener Python instalado (si deseas modificar el código o ejecutar scripts adicionales)
- El archivo `.env` debe estar configurado con las variables necesarias (ver más abajo).

## Instalación y uso

1. **Descargar y descomprimir** el archivo ZIP con la herramienta en tu dispositivo.
2. **Configurar el archivo `.env`**:
   - Dentro del archivo `.env`, asegúrate de configurar las variables adecuadas como:
     - `API_KEY` (tu clave API si es necesaria)
     - `OUTPUT_DIR` (directorio donde se guardarán los archivos Excel)
3. **Ejecutar la herramienta**:
   - Haz doble clic sobre `mipres_tool.exe` para abrir la aplicación y comenzar a procesar los archivos JSON.
4. **Resultado**:
   - Los archivos Excel generados se guardarán en el directorio que configuraste en el archivo `.env`.

## Variables de entorno (`.env`)

El archivo `.env` contiene las siguientes variables que debes configurar para el funcionamiento correcto de la herramienta:

API_URL_JUNTA_MEDICA=https://wsmipres.sispro.gov.co/WSMIPRESNOPBS/api/JuntaProfesionalXFecha
API_URL_PRESCRIPCION=https://wsmipres.sispro.gov.co/WSMIPRESNOPBS/api/Prescripcion
TOKEN= 
NIT=

> **Nota:** No subas el archivo `.env` a repositorios públicos, ya que contiene información sensible.

## Contacto

Si tienes alguna pregunta o necesitas soporte adicional, puedes contactarnos a: johnegutierrez14@gmail.com

---

¡Gracias por usar mipres-tools!