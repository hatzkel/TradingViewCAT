import hashlib

"""
Work in progress
"""

# Set this to something unique

pin = '1234'

# Generate unique token from pin. (This adds .... marginal security)
def get_token():
    token = hashlib.sha224(pin.encode('utf-8'))
    return token.hexdigest()