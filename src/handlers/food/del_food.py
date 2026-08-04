import os

from flask import current_app

from src.data import store


class FoodRemoveHandler:
    def remove(self, food_id):
        if not food_id:
            return {
                "status": False,
                "error": 1,
                "message": "food_id is required",
                "data": {},
            }, 400

        def remove_food(data):
            foods = data.setdefault("foods", [])
            food_item = next(
                (
                    item
                    for item in foods
                    if str(item.get("food_id")) == str(food_id)
                    or str(item.get("_id")) == str(food_id)
                ),
                None,
            )
            if not food_item:
                return {
                    "status": False,
                    "error": 1,
                    "message": f"No food item found with id {food_id}",
                    "data": {},
                }, 404

            image = food_item.get("image") or ""
            if image and not image.startswith(("http://", "https://")):
                upload_folder = current_app.config.get("UPLOAD_FOLDER", "src/assets")
                image_path = os.path.join(upload_folder, os.path.basename(image))
                if os.path.isfile(image_path):
                    os.remove(image_path)

            data["foods"] = [
                item
                for item in foods
                if str(item.get("food_id")) != str(food_id)
                and str(item.get("_id")) != str(food_id)
            ]
            return {
                "status": True,
                "error": 0,
                "message": f"Food item {food_id} removed successfully",
                "data": {},
            }, 200

        return store.update(remove_food)
