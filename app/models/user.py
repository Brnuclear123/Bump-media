from werkzeug.security import generate_password_hash

users = {
    'brand_a': {'password': generate_password_hash('demo123'), 'brand': 'Brand A'},
    'brand_b': {'password': generate_password_hash('demo123'), 'brand': 'Brand B'},
    'brand_c': {'password': generate_password_hash('demo123'), 'brand': 'Brand C'}
}
