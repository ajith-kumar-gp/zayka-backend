from flask import Flask, Blueprint,request
from src.handlers import CategoryAddHandler, CategoryGetHandler

category_blueprint = Blueprint("category", __name__)

@category_blueprint.route("/add", methods=["POST"])
def add_category():
    return CategoryAddHandler().create(request=request)

@category_blueprint.route("/list", methods=["GET"])
def list_category():
    return CategoryGetHandler().get_all()
