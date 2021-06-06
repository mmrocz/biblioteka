from flask import Flask, jsonify, make_response, abort, request
from models import biblioteka


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/api/v1/biblioteka/", methods=["GET"])
def biblioteka_list_api_v1():
    return jsonify(biblioteka.all())

@app.route("/api/v1/biblioteka/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = biblioteka.get(book_id)
    if not book:
        abort(404)
    return jsonify({"book": book})

@app.route("/api/v1/biblioteka/", methods=["POST"])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)

    book = {
        'author': request.json.get('author', 'None'),
        'id': biblioteka.all()[-1]['id'] + 1,
        'title': request.json['title'],
        'year': request.json.get('year', 0),
        'read': False
    }
    biblioteka.create(book)
    return jsonify({'book': book}), 201

@app.route("/api/v1/biblioteka/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    result = biblioteka.delete(book_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)



if __name__ == "__main__":
    app.run(debug=True)

