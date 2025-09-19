import os
import sys
sys.path.append('src')

from app import app, init_db

init_db()
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=False)