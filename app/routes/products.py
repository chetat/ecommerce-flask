from flask import render_template, request, jsonify
from . import bp
from app.models import Category, Product


"""
List most recent product and limit to 9 producta
in the home page
"""
@bp.route("/")
def homepage():
    categories = Category.query.all()
    products = Product.query.order_by(Product.created_at.desc()).all()

    last_created_products = products[:9]
    products_data = [product.serialize for product in last_created_products]
    categories_data = [category.serialize for category in categories]
    return render_template("home/index.html",
                           products=products_data, categories=categories_data)


"""
Get Single Product through product id
"""
@bp.route('/products/<product_id>', methods=['GET'])
def get_single_product(product_id):
    product = Product.query.get(product_id)
    return jsonify(product.serialize)


@bp.route('/products', methods=['POST'])
def create():
    name = request.json.get("name")
    stock = request.json.get("stock")
    price = request.json.get("price")
    description = request.json.get("description")
    category_id = request.json.get("category_id")
    image_url = request.json.get("image")
    new_product = Product(
        name=name,
        image=image_url,
        stock=stock,
        description=description,
        price=price,
        category_id=category_id
    )
    try:
        Product.insert(new_product)
    except Exception as e:
        print(e)
        return jsonify({
            "error": 500,
            "message": "Something went wrong"
        })
    return jsonify(
        new_product.serialize
    )


"""
Delete product in Database
"""
@bp.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    try:
        Product.delete(product)
    except Exception as e:
        print(e)
        return jsonify(
            {"error": 500,
             "message": "Problem deleting"}
        )
    return jsonify(
        {"success": True,
         "message": f"Product ID {product_id} deleted"}
    )


"""
Get Product Details by passing product ID
return: render product detail with product data
"""
@bp.route("/products/details/<product_id>")
def product_details(product_id):
    categories = Category.query.all()
    product = Product.query.filter_by(id=product_id).first()

    categories_data = [category.serialize for category in categories]
    return render_template("products/product_details.html",
                           product=product.serialize,
                           categories=categories_data)
