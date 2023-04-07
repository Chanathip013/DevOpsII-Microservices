from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

@app.route('/delete', methods=['POST'])
def delete():
    
    item = request.form.get('item')


    _item = us.item()
    data = [x for x in _item if x["item"]==item]


    if not data:
        return {"error": "Item not found"}, 401
    else:
        us.remove_item(item)
        return "Item removed successfully", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1