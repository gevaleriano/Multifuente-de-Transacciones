from datetime import datetime
from typing import Dict, Any, Tuple

STATUS_MAP = {
    "completed": "SUCCESS",
    "ok": "SUCCESS",
    "success": "SUCCESS",
    "failed": "FAILED",
    "error": "FAILED",
    "pending": "PENDING"
}

def clean_amount(raw_amount: Any, source_hint: str = "") -> Tuple[float, str]:
    if raw_amount is None:
        raise ValueError("Amount is missing")
    
    val_str = str(raw_amount).strip()
    detected_currency = ""
    
    if "€" in val_str:
        detected_currency = "EUR"
        val_str = val_str.replace("€", "")
    elif "$" in val_str:
        detected_currency = "USD"
        val_str = val_str.replace("$", "")
        
    val_str = val_str.replace(",", ".").strip()
    amount_float = float(val_str)
    
    if source_hint == "Fuente_Beta" or (isinstance(raw_amount, int) and amount_float > 1000):
        amount_float = amount_float / 100.0
        
    return round(amount_float, 2), detected_currency

def normalize_date(raw_date: Any) -> str:
    if not raw_date:
        raise ValueError("Date is missing")
    
    date_str = str(raw_date).strip()
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%d/%m/%Y %H:%M",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d"
    ]
    
    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            continue
            
    raise ValueError(f"Unrecognized date format: {date_str}")

def normalize_status(raw_status: Any) -> str:
    if not raw_status:
        return "PENDING"
    
    status_str = str(raw_status).strip().lower()
    return STATUS_MAP.get(status_str, "PENDING")

def detect_source_and_extract(raw_tx: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(raw_tx, dict):
        raise ValueError("Record is not a valid object")

    if "id" in raw_tx and "amount" in raw_tx and "timestamp" in raw_tx:
        raw_id = str(raw_tx.get("id"))
        raw_amount = raw_tx.get("amount")
        currency = str(raw_tx.get("currency", "USD")).upper()
        timestamp = raw_tx.get("timestamp")
        status = raw_tx.get("status")
        source = raw_tx.get("source", "Fuente_Alpha")
    elif "transaction_id" in raw_tx:
        raw_id = f"tx_{raw_tx.get('transaction_id')}"
        raw_amount = raw_tx.get("total")
        currency = str(raw_tx.get("currency_code", "USD")).upper()
        timestamp = raw_tx.get("created_at")
        status = raw_tx.get("state")
        source = "Fuente_Beta"
    elif "ref" in raw_tx:
        raw_id = str(raw_tx.get("ref"))
        raw_amount = raw_tx.get("amount")
        currency = ""
        timestamp = raw_tx.get("date")
        status = raw_tx.get("result")
        source = "Fuente_Gamma"
    else:
        raise ValueError("Unrecognized transaction schema")

    return {
        "raw_id": raw_id,
        "raw_amount": raw_amount,
        "currency": currency,
        "timestamp": timestamp,
        "status": status,
        "source": source
    }
