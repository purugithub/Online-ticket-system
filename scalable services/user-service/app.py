import sys
import os

# Add the parent directory of 'user_service' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

from user_service import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
