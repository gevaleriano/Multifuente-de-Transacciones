# Flujo del Aplicativo

```text
1. Carga Tolerante a Fallos --> Verificación y lectura de origin_transactions_alpha.json, beta.json y gamma.json (autocreación si faltan)
2. Consolidación            --> Generación/lectura de main_transactions.json
3. Normalización            --> Unificación de esquema, conversión a ISO-8601 y limpieza de monedas
4. Exploración Web          --> Interfaz responsiva con temas Light/Dark/System, filtros y DataTables
5. Export / Import          --> Descarga de plantilla JSON, exportación CSV y carga de nuevos lotes con validación estricta
```
