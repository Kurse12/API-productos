import json
import os
from flask import Blueprint, request, jsonify, Flask
from flask_jwt_extended import JWTManager
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
def get_product(id):
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
    data = request.json
    
    if not data.get("nombre") or not isinstance(data.get("precio"), (int, float)):
        return jsonify({"error": "Datos incompletos o invalidos"}), 400
    
    
    try:
        with get_cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                        INSERT INTO products (nombre,precio, descripcion, stock)
                        VALUES (%s, %s, %s, %s)
                        RETURNING id, nombre, precio, stock
                        """, (data["nombre"], data.get("precio", 0), data.get("descripcion", 0), data.get("stock", 0)))
            
            new_prod = cur.fetchone()
            conn.commit()
        return jsonify(new_prod), 201

    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
            
            

@api.route("/products/<int:id>", methods=["PATCH"])
@jwt_required()
def update_product(id):
    data = request.json

    if not data:
        return jsonify({"error": "No se enviaron datos para actualizar"}), 400

    if "precio" in data and not isinstance(data["precio"], (int, float)):
        return jsonify({"error": "Precio inválido"}), 400
    if "stock" in data and not isinstance(data["stock"], int):
        return jsonify({"error": "Stock inválido"}), 400
    if "nombre" in data and not isinstance(data["nombre"], str):
        return jsonify({"error": "Nombre inválido"}), 400
    if "descripcion" in data and not isinstance(data["descripcion"], str):
        return jsonify({"error": "Descripcion inválida"}), 400
    
    
    set_clause = []
    values = []

    for field in ["nombre", "precio", "descripcion", "stock"]:
        if field in data:
            set_clause.append(f"{field} = %s")
            values.append(data[field])

    if not set_clause:
        return jsonify({"error": "No hay campos válidos para actualizar"}), 400

    values.append(id)

    query = f"""
        UPDATE products
        SET {', '.join(set_clause)}
        WHERE id = %s
        RETURNING id, nombre, precio, descripcion, stock
    """

    try:
        with get_cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, values)
            updated_prod = cur.fetchone()
            if not updated_prod:
                return jsonify({"error": "Producto no encontrado"}), 404

            conn.commit()
        return jsonify(updated_prod), 200

    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500

@api.route("/products/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_product(id):
    try:
        with get_cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("DELETE FROM products WHERE id = %s RETURNING id, nombre, precio, descripcion, stock",(id,))
            
            deleted_prod = cur.fetchone()
            if not deleted_prod:
                return jsonify({"error":"Producto no encontrado"}), 404
            conn.commit()
            
        return jsonify({"Mensaje": "Producto eliminado", "producto":deleted_prod})
            
            
            
    except Exception as e:
        conn.rollback()
        return jsonify({"error":str(e)}), 500
