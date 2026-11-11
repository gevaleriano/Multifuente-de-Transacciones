# Sistema Multifuente de Normalización de Transacciones

Aplicación web responsiva desarrollada en Python con Flask y Tailwind CSS para consolidar, normalizar, validar y explorar registros financieros provenientes de tres fuentes heterogéneas (`origin_transactions_*.json`) hacia un repositorio maestro (`main_transactions.json`).

## Funcionalidades Principales
- **Consolidación Resiliente**: Lee los tres archivos de origen y los unifica en `data/main_transactions.json`. Si algún archivo de origen está vacío o no existe, lo regenera automáticamente sin lanzar errores.
- **Interfaz Responsiva y Multitema**: Soporte nativo para modo Claro (*Light*), Oscuro (*Dark*) y Sistema (*System*), adaptable a dispositivos móviles, tablets y escritorio.
- **Exploración Avanzada**: Tabla interactiva con búsqueda instantánea, paginación por iconos (`« ‹ 1 2 3 › »`), selector de registros por página (10 a 100) y exportación a CSV / portapapeles.
- **Exportar Plantilla e Importar**: Permite descargar una plantilla JSON (`plantilla_transacciones.json`) y subir nuevos lotes que se validan y anexan a `main_transactions.json`.

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
