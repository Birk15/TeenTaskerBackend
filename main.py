from app import create_app
from flask_cors import CORS
import os

app = create_app()

@app.route('/')
def home():
    return "Welcome to my Flask App!"

# Ermöglicht Frontend daten vom Backend zu laden 
CORS(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render verwendet eine PORT-Umgebungsvariable
    app.run(host='0.0.0.0', port=port)