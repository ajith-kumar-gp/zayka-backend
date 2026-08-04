import os

from flask import Blueprint, current_app, redirect, send_from_directory

showimage_blueprint = Blueprint("showimage", __name__)


@showimage_blueprint.route("/<path:filename>", methods=["GET"])
def serve_image(filename):
    if filename.startswith(("http://", "https://")):
        return redirect(filename)

    upload_folder = current_app.config.get("UPLOAD_FOLDER", "src/assets")
    return send_from_directory(upload_folder, os.path.basename(filename))
