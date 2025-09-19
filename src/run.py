import os
from app import app, init_db

print("Starting Student Management System...")
print(f"Current working directory: {os.getcwd()}")

# Initialize database
init_db()

# Get port from environment
port = int(os.environ.get('PORT', 5000))
print(f"Starting Flask app on port {port}...")

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)