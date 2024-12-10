from flask import request, jsonify
import base64
from app.config import get_collection

orders = get_collection("Orders")

def order_add():
    if 'image' not in request.files:
        return jsonify({"error": "Kein Bild hochgeladen!"}), 400

    image = request.files['image']  # Bild verarbeiten
    data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "title": request.form.get("title"),
        "description": request.form.get("description"),
        "price": request.form.get("price"),
        "image": image.read()  # Bild als Binärdaten speichern
    }

    orders.insert_one(data)  # Daten inkl. Bild in MongoDB speichern
    if not data:
        return jsonify({"error": "Keine Daten wurden gesendet!"}), 400
    return jsonify({"message": "Order erfolgreich hinzugefügt!"}), 201

def orders_get():
    try:
        # Alle Bestellungen aus der Collection holen
        data = list(orders.find({}))

        if data:
            for order in data:
                order["_id"] = str(order["_id"])  # Umwandlung der ObjectId in String
                if "image" in order:
                    # Umwandlung der Binärdaten in Base64-String
                    order["image"] = base64.b64encode(order["image"]).decode('utf-8')

            return jsonify({"data": data}), 200
        else:
            return jsonify({"message": "Keine Bestellungen gefunden!"}), 404
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify({"error": "Fehler beim Abrufen der Bestellungen"}), 500