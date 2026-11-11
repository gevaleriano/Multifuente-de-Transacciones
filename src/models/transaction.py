from dataclasses import dataclass
from typing import Optional

@dataclass
class Transaction:
    id: str
    amount: float
    currency: str
    timestamp: str
    status: str
    source: str
    is_valid: bool = True
    error_reason: Optional[str] = None
