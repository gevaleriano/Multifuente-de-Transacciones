from typing import List, Dict, Any
from models.transaction import Transaction

def calculate_metrics(transactions: List[Transaction]) -> Dict[str, Any]:
    total_processed = len(transactions)
    valid_txs = [t for t in transactions if t.is_valid]
    invalid_txs = [t for t in transactions if not t.is_valid]
    
    status_counts = {"SUCCESS": 0, "FAILED": 0, "PENDING": 0}
    totals_by_currency: Dict[str, float] = {}
    
    for t in valid_txs:
        status_counts[t.status] = status_counts.get(t.status, 0) + 1
        totals_by_currency[t.currency] = round(totals_by_currency.get(t.currency, 0.0) + t.amount, 2)
        
    return {
        "total_processed": total_processed,
        "valid_count": len(valid_txs),
        "invalid_count": len(invalid_txs),
        "status_counts": status_counts,
        "totals_by_currency": totals_by_currency
    }
