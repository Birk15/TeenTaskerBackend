from flask import Blueprint
from app.controllers.orderController import order_add, orders_get

orders_bp = Blueprint('orders', __name__)

@orders_bp.route("/add_order", methods=['POST'])
def add_order():
    return order_add()

@orders_bp.route("/get_orders", methods=['GET'])
def get_orders():
    return orders_get()

def setup_order_routes(app):
    app.register_blueprint(orders_bp)