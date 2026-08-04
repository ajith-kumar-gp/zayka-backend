import os

from flask import current_app
from werkzeug.utils import secure_filename

from src.data import store


class FoodAddHandler:
    def add(self, request):
        name = (request.form.get("name") or "").strip()
        price = request.form.get("price")
        category_id = request.form.get("category_id")
        category_name = (request.form.get("category") or "").strip()
        description = (request.form.get("description") or "").strip()
        image_url = (request.form.get("image_url") or "").strip()

        if not name or not price or not (category_id or category_name):
            return {
                "status": False,
                "error": 1,
                "message": "Missing required fields: name, price, and category",
                "data": {},
            }, 400

        try:
            price_value = float(price)
        except ValueError:
            return {
                "status": False,
                "error": 1,
                "message": "Price must be a number",
                "data": {},
            }, 400

        image = image_url
        uploaded_image = request.files.get("image")
        if uploaded_image and uploaded_image.filename:
            upload_folder = current_app.config.get("UPLOAD_FOLDER", "src/assets")
            os.makedirs(upload_folder, exist_ok=True)
            filename = secure_filename(uploaded_image.filename)
            image_path = os.path.join(upload_folder, filename)
            uploaded_image.save(image_path)
            image = filename

        def add_food(data):
            categories = data.setdefault("categories", [])
            foods = data.setdefault("foods", [])
            category = None

            if category_id:
                category = next(
                    (
                        item
                        for item in categories
                        if str(item.get("category_id")) == str(category_id)
                    ),
                    None,
                )

            if not category and category_name:
                category = next(
                    (
                        item
                        for item in categories
                        if item.get("name", "").lower() == category_name.lower()
                    ),
                    None,
                )

            if not category:
                return {
                    "status": False,
                    "error": 1,
                    "message": "Category not found",
                    "data": {},
                }, 404

            next_id = max((int(item.get("food_id", 0)) for item in foods), default=0) + 1
            food_item = {
                "_id": str(next_id),
                "food_id": next_id,
                "name": name,
                "price": price_value,
                "description": description,
                "image": image,
                "category": category["name"],
                "category_id": category["category_id"],
            }
            foods.append(food_item)
            return {
                "status": True,
                "error": 0,
                "message": "Food item added successfully",
                "data": food_item,
            }, 201

        return store.update(add_food)
