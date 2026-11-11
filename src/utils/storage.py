import json
import os
from typing import List, Dict, Any

ORIGIN_FILES = [
    "origin_transactions_alpha.json",
    "origin_transactions_beta.json",
    "origin_transactions_gamma.json"
]
MAIN_FILE = "main_transactions.json"

DEFAULT_ALPHA = [
    {"id": "tx_001", "amount": "325.12", "currency": "USD", "timestamp": "2025-03-10 08:15:00", "status": "pending"},
    {"id": "tx_002", "amount": "148.39", "currency": "USD", "timestamp": "2025-03-10 08:30:00", "status": "completed"}
]

DEFAULT_BETA = [
    {"transaction_id": 201, "total": 44454, "currency_code": "eur", "created_at": "10/03/2025 09:12", "state": "error"},
    {"transaction_id": 202, "total": 43629, "currency_code": "eur", "created_at": "10/03/2025 09:24", "state": "OK"}
]

DEFAULT_GAMMA = [
    {"ref": "A-01", "amount": "$214,95", "date": "2025-03-10T10:10:00Z", "result": "pending"},
    {"ref": "A-02", "amount": "€136,38", "date": "2025-03-10T10:30:00Z", "result": "success"}
]

def ensure_storage_files(data_dir: str) -> None:
    os.makedirs(data_dir, exist_ok=True)
    
    alpha_path = os.path.join(data_dir, "origin_transactions_alpha.json")
    if not os.path.exists(alpha_path) or os.path.getsize(alpha_path) == 0:
        with open(alpha_path, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_ALPHA, f, indent=2, ensure_ascii=False)

    beta_path = os.path.join(data_dir, "origin_transactions_beta.json")
    if not os.path.exists(beta_path) or os.path.getsize(beta_path) == 0:
        with open(beta_path, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_BETA, f, indent=2, ensure_ascii=False)

    gamma_path = os.path.join(data_dir, "origin_transactions_gamma.json")
    if not os.path.exists(gamma_path) or os.path.getsize(gamma_path) == 0:
        with open(gamma_path, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_GAMMA, f, indent=2, ensure_ascii=False)

def safe_read_json(filepath: str) -> List[Dict[str, Any]]:
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            data = json.loads(content)
            return data if isinstance(data, list) else []
    except Exception:
        return []

def consolidate_origin_files(data_dir: str) -> List[Dict[str, Any]]:
    ensure_storage_files(data_dir)
    main_path = os.path.join(data_dir, MAIN_FILE)
    
    if os.path.exists(main_path) and os.path.getsize(main_path) > 0:
        existing = safe_read_json(main_path)
        if existing:
            return existing

    consolidated: List[Dict[str, Any]] = []
    for filename in ORIGIN_FILES:
        file_path = os.path.join(data_dir, filename)
        records = safe_read_json(file_path)
        consolidated.extend(records)

    if not consolidated:
        consolidated = DEFAULT_ALPHA + DEFAULT_BETA + DEFAULT_GAMMA

    with open(main_path, "w", encoding="utf-8") as f:
        json.dump(consolidated, f, indent=2, ensure_ascii=False)

    return consolidated

def append_to_main_file(data_dir: str, new_records: List[Dict[str, Any]]) -> None:
    main_path = os.path.join(data_dir, MAIN_FILE)
    current_data = consolidate_origin_files(data_dir)
    current_data.extend(new_records)
    with open(main_path, "w", encoding="utf-8") as f:
        json.dump(current_data, f, indent=2, ensure_ascii=False)
