import sys, os
from app import app, db

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Ensure the database is initialized
with app.app_context():
    db.create_all()