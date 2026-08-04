# # src/handlers/cart_add_handler.py
# from flask import request, jsonify
# # from models.cart import Cart, db

# class CartAddHandler:
#     def __init__(self):
#         pass  # No special initialization needed here yet

#     def create(self, request):
#         try:
#             data = request.get_json()

#             user_id = data.get("user_id")
#             food_id = data.get("food_id")
#             food_name = data.get("food_name")
#             image = data.get("image")
#             price = data.get("price")
#             quantity = data.get("quantity", 1)

#             if not all([user_id, food_id, food_name, price]):
#                 return jsonify({"error": "Missing required fields"}), 400

#             # Check if item already exists in cart for the same user
#             existing_item = Cart.query.filter_by(user_id=user_id, food_id=food_id).first()
#             if existing_item:
#                 existing_item.quantity += quantity
#             else:
#                 new_cart_item = Cart(
#                     user_id=user_id,
#                     food_id=food_id,
#                     food_name=food_name,
#                     image=image,
#                     price=price,
#                     quantity=quantity
#                 )
#                 db.session.add(new_cart_item)

#             db.session.commit()

#             return jsonify({"message": "Item added to cart successfully"}), 201

#         except Exception as e:
#             return jsonify({"error": str(e)}), 500
