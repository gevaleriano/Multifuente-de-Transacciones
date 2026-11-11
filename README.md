# Sistema Multifuente de Normalización de Transacciones

Aplicación web desarrollada en Python con Flask y Tailwind CSS para consolidar, normalizar, validar y explorar registros financieros provenientes de tres fuentes heterogéneas (`origin_transactions_*.json`) hacia un repositorio maestro (`main_transactions.json`).

## Funcionalidades Principales
- **Consolidación Resiliente**: Lee los tres archivos de origen y los unifica en `data/main_transactions.json`. Si algún archivo de origen está vacío o no existe, continúa sin lanzar errores.
- **Exportar Plantilla**: Permite descargar un archivo JSON de ejemplo (`plantilla_transacciones.json`) con los formatos soportados.
- **Importar y Validar**: Permite subir nuevos archivos JSON, normalizarlos y agregarlos a `main_transactions.json`. Si el archivo no contiene ningún registro válido, muestra una alerta visual con enlace directo para descargar la plantilla.

## Pasos de Instalación y Ejecución

### Opción 1: Ejecución Local en Python
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/app.py
```
Acceder en el navegador a: `http://localhost:5000`

### Opción 2: Ejecución con Docker Compose
```bash
docker-compose up --build
```
Acceder en el navegador a: `http://localhost:5000`
