# Sistema Multifuente de Normalización de Transacciones

Aplicación web desarrollada en Python con Flask y Tailwind CSS para normalizar, validar y explorar registros financieros heterogéneos provenientes de múltiples fuentes.

## Requisitos
- Python 3.8+ o Docker / Docker Compose.

## Pasos de Instalación y Ejecución

### Opción 1: Ejecución Local en Python
```bash
python -m venv venv
source venv/bin/venv/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/app.py
```
Acceder en el navegador a: `http://localhost:5000`

### Opción 2: Ejecución con Docker Compose
```bash
docker-compose up --build
```
Acceder en el navegador a: `http://localhost:5000`

### Opción 3: Ejecución con Docker Directo
```bash
docker build -t transaction-normalizer .
docker run -p 5000:5000 transaction-normalizer
```
