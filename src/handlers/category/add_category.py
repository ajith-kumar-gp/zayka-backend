from src.data import store


class CategoryAddHandler:
    def create(self, request):
        body = request.get_json(silent=True) or {}
        name = (body.get("name") or "").strip()

        if not name:
            return {
                "status": False,
                "error": 1,
                "message": "Category name is required",
                "data": {},
            }, 400

        def add_category(data):
            categories = data.setdefault("categories", [])
            existing = next(
                (category for category in categories if category["name"].lower() == name.lower()),
                None,
            )
            if existing:
                return {
                    "status": False,
                    "error": 1,
                    "message": "Category already exists",
                    "data": {},
                }, 200

            next_id = max((category.get("category_id", 0) for category in categories), default=0) + 1
            category = {"category_id": next_id, "name": name}
            categories.append(category)
            return {
                "status": True,
                "error": 0,
                "message": "Category added successfully",
                "data": category,
            }, 201

        return store.update(add_category)
