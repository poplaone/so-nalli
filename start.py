#!/usr/bin/env python3
"""
Simple startup script for the Student Management System
"""
import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from app import app, init_db

if __name__ == '__main__':
    # Initialize database
    print("Initializing database...")
    init_db()
    print("Database initialized successfully!")
    
    # Get port from environment
    port = int(os.environ.get('PORT', 5000))
    
    print(f"Starting Flask app on port {port}...")
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False
    )