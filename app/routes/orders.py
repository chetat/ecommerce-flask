from flask import render_template, request, jsonify
from . import bp
from app.models import Cart, Category, Product, Order, OrderProduct, db, Address
from flask_login import login_user, logout_user, current_user, login_required

"""
Render Checkout page only if user is logged in, else
Render login page
"""
@bp.route("/checkout", methods=["GET"])
@login_required
def checkout_page():
    cart_items = Cart.query.all()
    total = []
    cart_products = []
    for item in cart_items:
        product = Product.query.filter_by(id=item.product_id).first()
        # Calculate product subtotal
        subtotal = item.quantity * product.serialize["price"]
        total.append(subtotal)
        cart_products.append({
            "name": product.serialize["name"],
            "id": product.serialize["id"],
            "price": product.serialize["price"],
            "image_url": product.serialize["image_url"],
            "description": product.serialize["description"],
            "quantity": item.quantity,
            "subtotal": item.quantity * product.serialize["price"]

        })
    return render_template("orders/checkout.html",
                           cart_items=cart_products, total=sum(total),
                           siz=len(cart_products))

"""
Create new Order
"""
@bp.route("/orders/create", methods=['POST'])
def create_order():
    payment_method = request.json.get("payment_method")
    country = request.json.get("country")
    zip_code = request.json.get("zip_code")
    city = request.json.get("state", None)
    user_id = request.json.get("user_id")

    # Create address object that will be saved in Order
    # Object
    address = Address(
        city=city,
        country=country,
        zip_code=zip_code)

    Address.insert(address)

    cart_items = Cart.query.all()

    total = []
    """
    Loop through cart items for given user 
    and calculate Order Total Amount
    """
    for item in cart_items:
        product = Product.query.filter_by(id=item.product_id).first()
        subtotal = item.quantity * product.serialize["price"]
        total.append(subtotal)

    order = Order(user_id=user_id,
                  payment_method=payment_method,
                  total_amount=sum(total),
                  address_id=address.id)

    Order.insert(order)
    products = [ci for ci in cart_items]

    order_products = []
    for prod in products:
        order_item = OrderProduct(
            order_id=order.id,
            product_id=prod.product_id,
            quantity=prod.quantity,
            user_id=user_id
        )
        OrderProduct.insert(order_item)
    # Clear Cart after Order has been created
    try:
        num_rows_deleted = db.session.query(Cart).delete()
        db.session.commit()
        print(num_rows_deleted)
    except Exception as e:
        db.session.rollback()
    print(order_products)
    return render_template("orders/order_complete.html",
                           ordered=order_products)

# List all user orders in db
@bp.route("/orders", methods=['GET'])
@login_required
def get_orders():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    orders_data = []
    for order in orders:
        order_prod = OrderProduct.query.filter_by(order_id=order.id).first()
        if order_prod:
            product = Product.query.filter_by(id=order_prod.product_id).first()
            temp = {
                "name": product.name,
                "price": product.price,
                "quantity": order_prod.quantity,
                "order_date": order.order_date.strftime("%b %d %Y %H:%M"),
                "total_amount": order.total_amount
            }
            orders_data.append(temp)
            print(order.id)
    print(orders_data)
    return render_template("orders/orders.html",
                           orders=orders_data, siz=len(orders_data))

# Render Completion page
@bp.route("/orders/complete")
def completed_order():
    return render_template("orders/order_complete.html")
