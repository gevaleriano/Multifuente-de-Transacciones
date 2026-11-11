import json
import os
from flask import Blueprint, render_template, request
from utils.validator import process_and_validate_transactions
from components.metrics_card import calculate_metrics

views_bp = Blueprint('views', __name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw_transactions.json')

def load_data():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

@views_bp.route('/')
def index():
    raw_data = load_data()
    all_transactions = process_and_validate_transactions(raw_data)
    
    status_filter = request.args.get('status', '').strip().upper()
    currency_filter = request.args.get('currency', '').strip().upper()
    source_filter = request.args.get('source', '').strip()
    validity_filter = request.args.get('validity', '').strip()

    filtered = all_transactions
    if status_filter:
        filtered = [t for t in filtered if t.status == status_filter]
    if currency_filter:
        filtered = [t for t in filtered if t.currency == currency_filter]
    if source_filter:
        filtered = [t for t in filtered if t.source == source_filter]
    if validity_filter == 'valid':
        filtered = [t for t in filtered if t.is_valid]
    elif validity_filter == 'invalid':
        filtered = [t for t in filtered if not t.is_valid]

    metrics = calculate_metrics(all_transactions)
    currencies = sorted(list(set(t.currency for t in all_transactions if t.currency)))
    sources = sorted(list(set(t.source for t in all_transactions if t.source)))

    return render_template(
        'dashboard.html',
        transactions=filtered,
        metrics=metrics,
        currencies=currencies,
        sources=sources,
        selected_status=status_filter,
        selected_currency=currency_filter,
        selected_source=source_filter,
        selected_validity=validity_filter
    )
