from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any

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

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
