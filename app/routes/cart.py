from flask import render_template, request, jsonify
from . import bp
from app.models import Category, Product, Cart
from flask_login import login_user, logout_user, current_user, login_required

"""
List all user's cart items
"""
@bp.route("/cart/all", methods=["GET"])
def view_cart_items():
    cart_items = Cart.query.all()
    total = []
    cart_products = []
    for item in cart_items:
        product = Product.query.filter_by(id=item.product_id).first()
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
    return render_template("cart/cart.html", cart_items=cart_products,
                           total=sum(total), siz=len(cart_products))

"""
Add Item to Cart and return all cart items
"""
@bp.route("/cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()
    print(data)
    product_id = request.json.get("product_id")
    quantity = request.json.get("quantity")
    user_id = request.json.get("user_id")

    cart_item = Cart(
        product_id=product_id,
        quantity=quantity,
        user_id=user_id
    )

    try:
        Cart.insert(cart_item)
    except Exception as e:
        print(e)
        return jsonify({
            "message": "could not add item to card"}), 500

    cart_items = Cart.query.all()

    return jsonify({
        "quantity": cart_item.serialize["quantity"],
        "product_id": cart_item.serialize["product_id"],
        "total_count": len(cart_items)
        })


"""
Get total number of items in cart
"""
@bp.route("/cart/count", methods=["GET"])
def cart_total():
    cart_items = Cart.query.all()
    return jsonify({
        "total": len(cart_items)
    })


"""
Update Cart Item
"""
@bp.route("/cart/update/<product_id>", methods=["PATCH"])
def update_cart(product_id):
    quantity = request.json.get("quantity")
    cart_item = Cart.query.filter_by(product_id=product_id).first()
    cart_item.quantity = quantity

    Cart.update(cart_item)
    cart_items = Cart.query.all()

    cart_products = []
    for item in cart_items:
        product = Product.query.filter_by(id=item.product_id).first()
        cart_products.append({
            "subtotal": item.quantity * product.serialize["price"]
        })
    cart_products.append(cart_item.serialize)
    return jsonify(
       cart_products
    )

"""
Delete Cart Item with Given ID
"""
@bp.route("/cart/delete/<product_id>", methods=["DELETE"])
def delete_cart(product_id):
    cart_item = Cart.query.filter_by(product_id=product_id).first()
    Cart.delete(cart_item)

    return jsonify(
        {
            "success": True,
            "message": "Item Deleted with success"
        }
    )
