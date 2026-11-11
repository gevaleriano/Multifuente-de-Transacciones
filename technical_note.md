# Technical Note

## MultiFuentes - Sistema Multifuentes de transacciones

## Decisiones de Diseño y Arquitectura

El sistema fue estructurado bajo un patrón modular desacoplado en Python (Flask), organizando las responsabilidades de forma estricta en carpetas separadas:

`models/`: Contiene la entidad de datos Transaction que estandariza el esquema unificado (id, amount, currency, timestamp, status, source).

`utils/`:

`storage.py`: Encargado de la lectura tolerante a fallos y la autocreación de archivos de origen (origin_transactions_*.json) y consolidación maestro (main_transactions.json).

`normalizer.py`: Funciones puras para la limpieza de montos, conversión de fechas a formato estricto ISO-8601, unificación de monedas y mapeo de estados.

`validator.py`: Reglas de validación estructural y tipado que separan registros válidos de inválidos sin interrumpir el flujo del sistema.

`components/`: Lógica de agregación para el cálculo de métricas financieras en tiempo real (totales procesados, tasas de éxito y sumatorias por moneda).

`views/`: Controladores de rutas en Flask para la gestión de filtros, exportación de plantillas y carga de nuevos archivos JSON.

## Principios de Ingeniería de Software Aplicados

**Single Responsibility Principle (SRP / SOLID)**: Cada módulo posee una única razón para cambiar (la persistencia está aislada en `storage.py`, la transformación en `normalizer.py` y el enrutamiento web en `routes.py`).

**KISS (Keep It Simple, Stupid)**: Evitamos dependencias externas innecesarias, utilizando exclusivamente la biblioteca estándar de Python y librerías ligeras aprobadas (Flask).

**DRY (Don't Repeat Yourself)**: Reutilización de funciones lógicas puras tanto en la consolidación inicial como en la importación dinámica vía interfaz web.

**YAGNI (You Aren't Gonna Need It)**: Se implementaron estrictamente los requerimientos solicitados por la rúbrica, sin añadir complejidad de bases de datos pesadas o microservicios innecesarios.

## Uso Estratégico de la IA y Delimitación de Responsabilidades

**Delegado a la IA**: Asistencia en la generación inicial de la estructura de las tablas responsivas con Tailwind CSS, el diseño de selectores y la integración de DataTables v2 con paginación segmentada e iconos.

**Controlado y Decidido por el Desarrollador**:

El esquema final de datos normalizados y las reglas de negocio (división de centavos para la Fuente Beta, limpieza de símbolos para la Fuente Gamma).

La arquitectura modular de carpetas (models, components, views, utils).

La estrategia de resiliencia ante la ausencia de archivos de origen (autocreación automática y tolerancia a fallos).

La eliminación de comentarios innecesarios en el código fuente para garantizar código limpio y expresivo.