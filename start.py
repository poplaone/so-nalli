#!/usr/bin/env python3
"""
Simple startup script for the Student Management System
"""
import os
import sys

# Add src to path - handle both local and Render environments
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

print(f"Current directory: {current_dir}")
print(f"Looking for app in: {src_path}")
print(f"Files in current dir: {os.listdir(current_dir)}")
if os.path.exists(src_path):
    print(f"Files in src dir: {os.listdir(src_path)}")

try:
    from app import app, init_db
    print("Successfully imported app and init_db")
except ImportError as e:
    print(f"Import error: {e}")
    print("Trying alternative import...")
    # Try alternative import path
    sys.path.insert(0, current_dir)
    try:
        from src.app import app, init_db
        print("Successfully imported with src.app")
    except ImportError as e2:
        print(f"Alternative import also failed: {e2}")
        sys.exit(1)

if __name__ == '__main__':
    # Initialize database
    print("Initializing database...")
    try:
        init_db()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Database initialization error: {e}")
    
    # Get port from environment
    port = int(os.environ.get('PORT', 5000))
    
    print(f"Starting Flask app on port {port}...")
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False
    )