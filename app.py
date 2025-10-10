from flask import Flask
from routes import api
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
