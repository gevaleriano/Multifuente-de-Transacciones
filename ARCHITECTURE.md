# Arquitectura del Sistema de Normalización de Transacciones

## 1. Visión General
El sistema implementa una arquitectura modular desacoplada en Python utilizando Flask y Tailwind CSS, organizando las responsabilidades en `models`, `components`, `views` y `utils`.

```text
[Cliente Web] <---> [Views / Routes (Flask)] <---> [Storage / Validator / Normalizer] <---> [Data Layer (JSON)]
                                                               |
                                                               v
                                                       [Models (Transaction)]
```

## 2. Capas y Componentes
- **Models (`src/models/transaction.py`)**: Entidad `Transaction` con esquema normalizado unificado.
- **Utils (`src/utils/`)**:
  - `storage.py`: Lectura tolerante a fallos de los archivos de origen (`origin_transactions_*.json`), consolidación en `main_transactions.json` y anexado de cargas nuevas.
  - `normalizer.py`: Detección de esquema de origen y transformación pura de montos, fechas (ISO-8601), monedas y estados.
  - `validator.py`: Validación estructural y de tipos sin interrumpir el procesamiento masivo.
- **Components (`src/components/metrics_card.py`)**: Agregación de métricas financieras en tiempo real.
- **Views (`src/views/routes.py`)**: Controlador web para filtrado, exportación de plantilla JSON e importación de archivos.
