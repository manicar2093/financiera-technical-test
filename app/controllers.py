from flask import Blueprint, request, jsonify
from app.services import InMemoryService

inmem = Blueprint("inmem", __name__, url_prefix= "/inmem")

dbInMemory = dict()

@inmem.route("", methods=["PUT"])
def put_inmem():

    try:
        item = request.get_json()

        # Se valida que el body contenga los datos necesarios. Detalles en el README.md
        valid = item.get("key")
        if not valid:
            return jsonify({"message": "Key not found in body. Consider request's documentation"}), 400
        valid = item.get("value")
        if not valid:
            return jsonify({"message": "Value not found in body. Consider request's documentation"}), 400
        
        in_memory_service = InMemoryService()
        inserted = in_memory_service.add_inmemory_item(item, dbInMemory)
        
        return jsonify(inserted.to_dict()), 201

    except Exception:
        return jsonify({"message": "An unexpected error has occured"}), 500

    

@inmem.route("/<key>", methods=["GET"])
def get_inmem_key(key):
    try:
        
        in_memory_service = InMemoryService()
        found = in_memory_service.get_inmemory_item(key, dbInMemory)
        
        return jsonify(found.to_dict()), 200

    except KeyError:
        return jsonify({"message": f"There is no value nor version for key '{key}'"}), 404

    except Exception:
        return jsonify({"message": "An unexpected error has occured"}), 500
    
@inmem.route("/<key>/<int:version>", methods=["GET"])
def get_inmem(key, version: int):
    try:
        
        in_memory_service = InMemoryService()
        found = in_memory_service.get_inmemory_item(key, dbInMemory, version=version)
        
        return jsonify(found.to_dict()), 200

    except KeyError:
        return jsonify({"message": f"There is no value for key '{key}' with version {version}"}), 404

    except Exception:
        return jsonify({"message": "An unexpected error has occured"}), 500