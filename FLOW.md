# Flujo del Aplicativo

```text
1. Carga Tolerante a Fallos --> Lectura de origin_transactions_alpha.json, beta.json y gamma.json (ignora vacíos/inexistentes)
2. Consolidación            --> Generación/lectura de main_transactions.json
3. Normalización            --> Unificación de esquema, conversión a ISO-8601 y limpieza de monedas
4. Exploración Web          --> Filtrado interactivo por estado, moneda, fuente y validez
5. Export / Import          --> Descarga de plantilla JSON y carga de nuevos lotes con validación estricta
```
