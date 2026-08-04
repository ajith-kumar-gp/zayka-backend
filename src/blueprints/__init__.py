# from .home import home_blueprint
# def register_blueprints(app):
#     app.register_blueprint(home_blueprint, url_prefix = "/home")




from .food import food_blueprint
from .category import category_blueprint
from .showimage import showimage_blueprint
from .user import user_blueprint
from .order import order_blueprint
# from .cart import cart_blueprint


def register_blueprints(app):
    app.register_blueprint(food_blueprint, url_prefix = "/food")
    app.register_blueprint(category_blueprint, url_prefix = "/category")
    app.register_blueprint(showimage_blueprint, url_prefix = "/showimage")
    app.register_blueprint(user_blueprint, url_prefix = "/user")
    app.register_blueprint(order_blueprint, url_prefix = "/order")
    # app.register_blueprint(cart_blueprint, url_prefix = "/cart")
