# Arquitectura del Sistema de Normalización de Transacciones

## 1. Visión General
El sistema implementa una arquitectura modular MVC (Modelo-Vista-Controlador) desacoplada en Python utilizando Flask y Tailwind CSS.

```text
[Cliente Web] <---> [Views / Routes (Flask)] <---> [Validator / Normalizer] <---> [Data Layer (JSON)]
                                                         |
                                                         v
                                                 [Models (Transaction)]
```

## 2. Componentes Principales
- **Models (`src/models/transaction.py`)**: Entidad de datos `Transaction` que encapsula la estructura normalizada.
- **Utils (`src/utils/`)**:
  - `normalizer.py`: Funciones puras para detectar fuentes, transformar fechas, limpiar montos y unificar estados.
  - `validator.py`: Reglas de validación que separan registros válidos de defectuosos.
- **Components (`src/components/metrics_card.py`)**: Cálculo de agregaciones y métricas financieras en tiempo real.
- **Views (`src/views/routes.py`)**: Controladores que reciben filtros web y sirven los datos a la plantilla HTML estilizada con Tailwind CSS.
