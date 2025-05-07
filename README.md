
# mipres-tools 🛠️📄

**mipres-tools** es una aplicación de escritorio desarrollada en Python con interfaz gráfica (Tkinter), diseñada para facilitar la descarga, procesamiento y exportación de archivos JSON del sistema **MIPRES** (Ministerio de Salud de Colombia), incluyendo prescripciones y juntas médicas. Esta herramienta convierte los datos en archivos Excel estructurados y listos para análisis en herramientas como Power BI.

---

## 🧩 Características

- ✅ Descarga automatizada de archivos JSON desde el sistema MIPRES.
- ✅ Procesamiento y conversión a formatos Excel legibles.
- ✅ Interfaz gráfica amigable y soporte por consola.
- ✅ Estructura modular y escalable.
- ✅ Ideal para profesionales de salud, analistas de datos y áreas de planeación.

---

## 📂 Estructura del proyecto

```
mipres-tools/
├── assets/
├── mipres_tool/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py                       # Archivo principal (GUI + CLI)
│   ├── interfaces/                   # Componentes gráficos (Tkinter)
│   │   └── __init__.py
│   │   └── gui.py
│   ├── handlers/                     # Lógica de negocio (descarga, parseo, exportación)
│   │   └── __init__.py
│   │   └── juntas_medicas.py
│   │   └── prescripciones.py
│   └── utils/                        # Funciones auxiliares (helpers, validaciones)
│       └── __init__.py
│       └── helpers.py
│       └── procesar_juntas_medicas.py
│       └── procesar_prescripcion.py
├── .env
├── .gitignore
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Documentación
└── LICENSE                    # Licencia MIT
```

---

## 🚀 Instalación

### Requisitos previos
- Python 3.11 o superior
- pip

### Clonar el repositorio

```bash
git clone https://github.com/johngutierrez14/mipres-tools.git
cd mipres-tools
```

### Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución

### Opción 1: Usar interfaz gráfica

```bash
python -m mipres_tool.main
```

### Opción 2: Desde consola

```bash
python -m mipres_tool.main --modo consola
```

---

## 📊 Casos de uso

Descarga automática de archivos JSON desde la API del sistema MIPRES (prescripciones y juntas médicas).
Limpieza y transformación de datos crudos a formatos tabulares claros y estandarizados.
Conversión de datos a archivos Excel (.xlsx) para su análisis individual o distribución institucional.
Preparación de datos para integración directa con herramientas de Business Intelligence como Power BI, Looker Studio, etc.


---

## 👩‍💻 Contribuciones

¿Tienes ideas, mejoras o quieres colaborar?

1. Haz un fork del proyecto.
2. Crea una nueva rama: `git checkout -b feature/mi-mejora`
3. Haz tus cambios y realiza commits descriptivos.
4. Envía un Pull Request.

---

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.

---