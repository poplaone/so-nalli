"""
WSGI Entry Point for Render Deployment
"""
import os
import sys

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

print(f"WSGI: Current directory: {current_dir}")
print(f"WSGI: Looking for app in: {src_path}")

try:
    from app import app, init_db
    print("WSGI: Successfully imported app and init_db")
except ImportError as e:
    print(f"WSGI: Import error: {e}")
    # Try alternative import
    sys.path.insert(0, current_dir)
    from src.app import app, init_db
    print("WSGI: Successfully imported with src.app")

# Initialize database on startup
try:
    init_db()
    print("WSGI: Database initialized successfully!")
except Exception as e:
    print(f"WSGI: Database initialization error: {e}")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)