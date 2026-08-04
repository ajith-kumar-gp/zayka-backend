from datetime import datetime, timezone

from flask import Blueprint, request

from src.data import store

order_blueprint = Blueprint("order", __name__)


@order_blueprint.route("/place", methods=["POST"])
def place_order():
    body = request.get_json(silent=True) or {}
    items = body.get("items") or []
    delivery_info = body.get("deliveryInfo") or {}
    total_amount = body.get("totalAmount")

    if not items:
        return {
            "status": False,
            "error": 1,
            "message": "Cart is empty",
            "data": {},
        }, 400

    required_fields = ["firstName", "lastName", "email", "street", "city", "state", "zipCode", "country", "phone"]
    missing_fields = [field for field in required_fields if not delivery_info.get(field)]
    if missing_fields:
        return {
            "status": False,
            "error": 1,
            "message": f"Missing delivery fields: {', '.join(missing_fields)}",
            "data": {},
        }, 400

    def save_order(data):
        orders = data.setdefault("orders", [])
        next_id = max((int(order.get("order_id", 0)) for order in orders), default=0) + 1
        order = {
            "order_id": next_id,
            "items": items,
            "deliveryInfo": delivery_info,
            "totalAmount": total_amount,
            "status": "Pending",
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        orders.append(order)
        return {
            "status": True,
            "error": 0,
            "message": "Order placed successfully",
            "data": order,
        }, 201

    return store.update(save_order)
