from flask import Blueprint, request, jsonify
import jwt
from models import db, Product
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)

@api.route("/products",methods=["GET"])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@api.route("/products/<int:id>", methods=["GET"])
@jwt_required()
def get_product():
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict())


@api.route("/products", methods=["POST"])
@jwt_required()
def create_product():
    return

@api.route("/products/<int:id>", methods=["PUT"])
@jwt_required()
def update_product(id):
    return

@api.route("/prodcuts/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_product(id):
    return
