# from flask import Flask, Blueprint,request
# from src.handlers import CartAddHandler, CartDelHandler, CartGetHandler  


# cart_blueprint = Blueprint("cart", __name__, url_prefix="/cart")

# @cart_blueprint.route("/add", methods=["POST"])
# def add_cart_item():
#     return CartAddHandler().create(request=request)

# @cart_blueprint.route("/delete/<int:item_id>", methods=["DELETE"])
# def delete_cart_item(item_id):
#     return CartDelHandler().remove_from_cart(item_id=item_id)

# @cart_blueprint.route("/list/<int:user_id>", methods=["GET"])
# def list_cart_items(user_id):
#     return CartGetHandler().get_all(user_id=user_id)