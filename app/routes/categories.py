from flask import render_template, request, jsonify
from . import bp
from app.models import Category, Product, Cart

"""
List all categories in database
"""
@bp.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    return jsonify([category.serialize for category in categories])


"""
Create a new Category
"""
@bp.route("/categories", methods=["POST"])
def create_category():
    name = request.json.get("name")
    description = request.json.get('description')
    category = Category(name=name, description=description)

    try:
        Category.insert(category)
    except Exception as e:
        print(e)

    return jsonify(category.serialize)

"""
Delete a Category with given ID
"""
@bp.route('/categories/<category_id>', methods=['DELETE'])
def delete_categories(category_id):
    category = Category.query.get(category_id)
    try:
        Category.delete(category)
    except Exception as e:
        print(e)
        return jsonify(
            {"error": 500,
             "message": "Problem deleting category"}
        )
    return jsonify(
        {"success": True,
         "message": f"Product ID {category_id} deleted"}
    )


"""
Get All products belonging to a given category ID
"""
@bp.route("/products/categories/<category_id>")
def products_by_categoryId(category_id):
    products = Product.query.filter_by(category_id=category_id).all()
    products_data = [product.serialize for product in products]

    categories = Category.query.all()
    categories_data = [category.serialize for category in categories]
    print(len(categories_data))

    return render_template("home/index.html", products=products_data, categories=categories_data)
