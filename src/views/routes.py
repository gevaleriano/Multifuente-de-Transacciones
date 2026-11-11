import json
import os
from flask import Blueprint, render_template, request, Response, redirect, url_for, flash
from utils.validator import process_and_validate_transactions
from utils.storage import consolidate_origin_files, append_to_main_file
from components.metrics_card import calculate_metrics

views_bp = Blueprint('views', __name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

@views_bp.route('/')
def index():
    raw_data = consolidate_origin_files(DATA_DIR)
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

@views_bp.route('/export-template')
def export_template():
    template_data = [
        {
            "id": "tx_901",
            "amount": "125.50",
            "currency": "USD",
            "timestamp": "2025-03-15 10:30:00",
            "status": "completed"
        },
        {
            "transaction_id": 902,
            "total": 8500,
            "currency_code": "usd",
            "created_at": "15/03/2025 11:00",
            "state": "OK"
        },
        {
            "ref": "A-903",
            "amount": "€49,99",
            "date": "2025-03-15T12:00:00Z",
            "result": "success"
        }
    ]
    json_str = json.dumps(template_data, indent=2, ensure_ascii=False)
    return Response(
        json_str,
        mimetype='application/json',
        headers={'Content-Disposition': 'attachment;filename=plantilla_transacciones.json'}
    )

@views_bp.route('/import', methods=['POST'])
def import_transactions():
    uploaded_file = request.files.get('file')
    if not uploaded_file or uploaded_file.filename == '':
        flash("Formato inválido, si gusta puede descargar plantilla de carga.", "error")
        return redirect(url_for('views.index'))

    try:
        raw_content = uploaded_file.read().decode('utf-8').strip()
        if not raw_content:
            flash("Formato inválido, si gusta puede descargar plantilla de carga.", "error")
            return redirect(url_for('views.index'))

        parsed_data = json.loads(raw_content)
        if not isinstance(parsed_data, list) or len(parsed_data) == 0:
            flash("Formato inválido, si gusta puede descargar plantilla de carga.", "error")
            return redirect(url_for('views.index'))

        validated = process_and_validate_transactions(parsed_data)
        valid_records = [tx for tx in validated if tx.is_valid]

        if len(valid_records) == 0:
            flash("Formato inválido, si gusta puede descargar plantilla de carga.", "error")
            return redirect(url_for('views.index'))

        append_to_main_file(DATA_DIR, parsed_data)
        flash(f"Se importaron y consolidaron {len(parsed_data)} registros ({len(valid_records)} válidos) correctamente.", "success")
    except Exception:
        flash("Formato inválido, si gusta puede descargar plantilla de carga.", "error")

    return redirect(url_for('views.index'))
