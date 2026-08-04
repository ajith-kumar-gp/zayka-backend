# from flask import Flask
# from .app import FlaskEnv


# def initconfig(app: Flask):
#     app.config.update(
#         SQLALCHEMY_DATABASE_URI=FlaskEnv.DATABASE_URI
#     )


import os

from flask import Flask
from dotenv import load_dotenv



def initconfig(app: Flask):
    load_dotenv()

    backend_root = os.path.abspath(os.path.join(app.root_path, ".."))
    app.config.update(
        SECRET_KEY=os.getenv("SECRET_KEY", "zayka-local-dev-secret"),
        UPLOAD_FOLDER=os.getenv(
            "UPLOAD_FOLDER",
            os.path.join(backend_root, "src", "assets"),
        ),
        DATA_FILE=os.getenv(
            "DATA_FILE",
            os.path.join(backend_root, "src", "data", "zayka_data.json"),
        ),
    )


