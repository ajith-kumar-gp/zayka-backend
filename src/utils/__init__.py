from flask import Flask, app
from flask_cors import CORS

from src.blueprints import register_blueprints
from src.config import initconfig
from src.data import store
from pathlib import Path


def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": "*"}})
    initconfig(app)
    store.path = Path(app.config["DATA_FILE"]).resolve()
    store.ensure()
    register_blueprints(app)

    @app.get("/")
    def health():
        return {"status": True, "message": "Zayka backend is running"}

    return app
