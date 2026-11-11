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

## 2. Reglas de Transformación por Archivo de Origen
- **`origin_transactions_alpha.json` (`Fuente_Alpha`)**: Campos `id`, `amount`, `currency`, `timestamp` (`YYYY-MM-DD HH:MM:SS`), `status`.
- **`origin_transactions_beta.json` (`Fuente_Beta`)**: Campos `transaction_id` (prefijado con `tx_`), `total` (centavos divididos entre 100), `currency_code`, `created_at` (`DD/MM/YYYY HH:MM`), `state`.
- **`origin_transactions_gamma.json` (`Fuente_Gamma`)**: Campos `ref`, `amount` (limpieza de símbolos `€`/`$` y coma decimal), `date` (ISO-8601), `result`.
