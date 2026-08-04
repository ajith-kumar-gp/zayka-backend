from src.data import store


class FoodListHandler:
    def list(self):
        data = store.read()
        return data.get("foods", [])
