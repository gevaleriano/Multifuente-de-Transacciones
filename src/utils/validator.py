from typing import Dict, Any, List
from models.transaction import Transaction
from utils.normalizer import detect_source_and_extract, clean_amount, normalize_date, normalize_status

def process_and_validate_transactions(raw_transactions: List[Dict[str, Any]]) -> List[Transaction]:
    processed = []
    if not isinstance(raw_transactions, list):
        return processed
    
    for item in raw_transactions:
        try:
            extracted = detect_source_and_extract(item)
            amount, detected_curr = clean_amount(extracted["raw_amount"], extracted["source"])
            currency = extracted["currency"] or detected_curr or "USD"
            iso_date = normalize_date(extracted["timestamp"])
            norm_status = normalize_status(extracted["status"])
            
            tx = Transaction(
                id=extracted["raw_id"],
                amount=amount,
                currency=currency,
                timestamp=iso_date,
                status=norm_status,
                source=extracted["source"],
                is_valid=True
            )
        except Exception as err:
            fallback_id = "ERR"
            fallback_src = "Desconocida"
            if isinstance(item, dict):
                fallback_id = str(item.get("id") or item.get("transaction_id") or item.get("ref") or "ERR")
                if "transaction_id" in item:
                    fallback_src = "Fuente_Beta"
                elif "ref" in item:
                    fallback_src = "Fuente_Gamma"
                elif "id" in item:
                    fallback_src = "Fuente_Alpha"
            tx = Transaction(
                id=fallback_id,
                amount=0.0,
                currency="USD",
                timestamp="",
                status="FAILED",
                source=fallback_src,
                is_valid=False,
                error_reason=str(err)
            )
            
        processed.append(tx)
        
    return processed
