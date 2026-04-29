"""
Financial transaction models for FinTech service.
Handles payment records, fraud flags, and audit trails.
"""

class Transaction:
    """Core financial transaction record"""
    transaction_id: str
    sender_account: str
    receiver_account: str
    amount: float
    currency: str
    transaction_type: str  # transfer, payment, refund
    status: str  # pending, processing, completed, failed, flagged
    fraud_score: float
    created_at: str
    processed_at: str


class FraudAlert:
    """Fraud detection alert records"""
    alert_id: str
    transaction_id: str
    alert_type: str  # velocity, pattern, blacklist
    risk_level: str  # low, medium, high, critical
    action_taken: str  # allow, block, review
    reviewed_by: str
    created_at: str


class AuditLog:
    """PCI-DSS compliance audit trail"""
    log_id: str
    transaction_id: str
    action: str
    actor_id: str
    ip_address: str
    timestamp: str
    details: str
