import json
import os
from typing import List, Dict, Any

ORIGIN_FILES = [
    "origin_transactions_alpha.json",
    "origin_transactions_beta.json",
    "origin_transactions_gamma.json"
]
MAIN_FILE = "main_transactions.json"

def safe_read_json(filepath: str) -> List[Dict[str, Any]]:
    if not os.path.exists(filepath):
        return []
    if os.path.getsize(filepath) == 0:
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

    with open(main_path, "w", encoding="utf-8") as f:
        json.dump(consolidated, f, indent=2, ensure_ascii=False)

    return consolidated

def append_to_main_file(data_dir: str, new_records: List[Dict[str, Any]]) -> None:
    main_path = os.path.join(data_dir, MAIN_FILE)
    current_data = consolidate_origin_files(data_dir)
    current_data.extend(new_records)
    with open(main_path, "w", encoding="utf-8") as f:
        json.dump(current_data, f, indent=2, ensure_ascii=False)
