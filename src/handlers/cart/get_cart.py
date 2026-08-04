# from flask import request, jsonify
# from models.cart import Cart, db
# from datetime import datetime


# class CartGetHandler:
#     def get_all(self, request):
#         try:
#             user_id = request.args.get("user_id")
#             if not user_id:
#                 return jsonify({"error": "User ID is required"}), 400

#             cart_items = Cart.query.filter_by(user_id=user_id).all()
#             items_list = [
#                 {
#                     "id": item.id,
#                     "food_id": item.food_id,
#                     "food_name": item.food_name,
#                     "image": item.image,
#                     "price": item.price,
#                     "quantity": item.quantity,
#                     "created_at": item.created_at
#                 }
#                 for item in cart_items
#             ]

#             return jsonify({"cart_items": items_list}), 200

#         except Exception as e:
#             return jsonify({"error": str(e)}), 500
