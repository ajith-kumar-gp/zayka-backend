# from flask import request, jsonify
# from models.cart import Cart, db

# class CartDelHandler:
#     def __init__(self):
#         pass

#     def remove_from_cart(self):
#         try:
#             data = request.get_json()
#             user_id = data.get("user_id")
#             food_id = data.get("food_id")

#             if not all([user_id, food_id]):
#                 return jsonify({"error": "Missing required fields"}), 400

#             cart_item = Cart.query.filter_by(user_id=user_id, food_id=food_id).first()

#             if not cart_item:
#                 return jsonify({"error": "Item not found in cart"}), 404


#             db.session.delete(cart_item)
#             db.session.commit()

#             return jsonify({"message": "Item removed from cart successfully"}), 200

#         except Exception as e:
#             return jsonify({"error": str(e)}), 500
