# Especificación de Normalización de Datos

## 1. Esquema Objetivo Unificado
```json
{
  "id": "string",
  "amount": 99.99,
  "currency": "USD",
  "timestamp": "ISO-8601",
  "status": "SUCCESS | FAILED | PENDING",
  "source": "string"
}
```

## 2. Reglas de Mapeo por Fuente
- **Fuente Alpha (`id`, `amount`, `currency`, `timestamp`, `status`)**: Mapeo directo; conversión de fecha `YYYY-MM-DD HH:MM:SS` a ISO-8601.
- **Fuente Beta (`transaction_id`, `total`, `currency_code`, `created_at`, `state`)**: Mapeo de `transaction_id` a `tx_<id>`; división de `total` en centavos entre 100; conversión de fecha `DD/MM/YYYY HH:MM`.
- **Fuente Gamma (`ref`, `amount`, `date`, `result`)**: Limpieza de cadenas con moneda integrada (`€99,99`); estandarización de estado.
