from flask import Flask
from flask_jwt_extended import JWTManager
from routes import api
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

jwt = JWTManager(app)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
