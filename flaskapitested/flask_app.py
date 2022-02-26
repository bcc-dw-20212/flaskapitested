"""A ideia de usar testes é que código, de certa forma, documenta a lógica do código.

    Por isso, familizarize-se com os testes para já ter esse hábito.

    Mas a API ainda precisa de documentação, por isso, vamos em breve ver o Swagger.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

resource = {}


@app.get("/")
def root():
    return jsonify(resource), 200


@app.get("/<int:id>")
def get_by_id(id):
    if id in resource:
        return jsonify(resource[id]), 200
    else:
        return jsonify({}), 404


@app.post("/")
def post_to_resource():
    newobj = request.get_json()
    resource[len(resource)] = newobj

    return jsonify(resource[len(resource) - 1]), 200


@app.delete("/<int:id>")
def delete_from_resource(id):
    if id in resource:
        del resource[id]
        return jsonify({}), 200
    else:
        return jsonify({}), 404


@app.put("/<int:id>")
def update_resource(id):
    if id in resource:
        newobj = request.get_json()
        resource[id] = newobj
        return jsonify(resource[id]), 200
    else:
        return jsonify({}), 404
