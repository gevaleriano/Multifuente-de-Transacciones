from typing import Dict, Any, List
from models.transaction import Transaction
from utils.normalizer import detect_source_and_extract, clean_amount, normalize_date, normalize_status

def process_and_validate_transactions(raw_transactions: List[Dict[str, Any]]) -> List[Transaction]:
    processed = []
    
    for item in raw_transactions:
        extracted = detect_source_and_extract(item)
        
        try:
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
            tx = Transaction(
                id=extracted["raw_id"] or "ERR",
                amount=0.0,
                currency=extracted["currency"] or "USD",
                timestamp=str(extracted["timestamp"] or ""),
                status="FAILED",
                source=extracted["source"],
                is_valid=False,
                error_reason=str(err)
            )
            
        processed.append(tx)
        
    return processed
