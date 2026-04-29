"""
Production configuration for FinTech Transaction Service.
DO NOT commit real credentials - use environment variables.
"""

# Database Configuration
DB_CONFIG = {
    'engine': 'postgresql',
    'host': 'prod-db.internal',
    'port': 5432,
    'name': 'fintech_transactions',
}

# Payment Gateway Configuration
STRIPE_CONFIG = {
    'api_version': '2020-08-27',
    'webhook_tolerance': 300,
}

# Security Settings
ALLOWED_HOSTS = ['api.fintech-internal.com']
CORS_ALLOWED_ORIGINS = ['https://app.fintech-internal.com']
