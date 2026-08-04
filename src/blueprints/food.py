from flask import Flask, Blueprint,request
from src.handlers import FoodListHandler, FoodAddHandler, FoodRemoveHandler
import os

food_blueprint = Blueprint("food", __name__)


@food_blueprint.route("/list", methods=["GET"])
def list_food():
    return FoodListHandler().list()


@food_blueprint.route("/add",methods=["POST"])
def add_food():
    return FoodAddHandler().add(request=request)


@food_blueprint.route("/remove", methods=["DELETE"])
def remove_food():
    data = request.get_json()
    food_id = data.get("food_id")
    handler = FoodRemoveHandler()
    response, status = handler.remove(food_id)
    return response, status



