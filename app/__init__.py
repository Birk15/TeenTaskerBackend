from flask import Flask
from app.config import Config
from app.routes.userRoutes import setup_user_routes
from app.routes.orderRoute import setup_order_routes

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    setup_user_routes(app)
    setup_order_routes(app)

    return app