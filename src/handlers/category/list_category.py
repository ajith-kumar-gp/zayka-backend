from src.data import store


class CategoryGetHandler:
    def get_all(self):
        data = store.read()
        return {
            "status": True,
            "error": 0,
            "message": "Categories fetched successfully",
            "data": data.get("categories", []),
        }
