import json
from flask import Blueprint, request, jsonify
import jwt
import psycopg2
from db import get_cursor,conn
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)

@api.route("/products",methods=["GET"])
@jwt_required()
def get_products():
    try:
        with get_cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM products")
            prods = cur.fetchall()
            return jsonify(prods)
    except Exception as e:
        return jsonify({"error":str(e)}), 500


@api.route("/products/<int:id>", methods=["GET"])
@jwt_required()
def get_product():
    try:
        with get_cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM products WHERE id = %s", (id,))
            prod = cur.fetchone()
            if prod:
                return jsonify(prod)
            else:
                return jsonify({"Error":"Producto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error":str(e)}), 500


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
