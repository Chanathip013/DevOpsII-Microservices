from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

def _find_item(item):
    data = [x for x in item if x["item"]==item]
    return data

@app.route('/put', methods=['POST'])
def put():
    item = request.form.get('item')

    _item = us.find_item(item)
    data = [x for x in _item if x["item"]==item]
    if (data):
        return jsonify({'message': 'Created successfully.'}), 200
    else:
        return jsonify({'message': 'Cannot create.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) #127.0.0.1