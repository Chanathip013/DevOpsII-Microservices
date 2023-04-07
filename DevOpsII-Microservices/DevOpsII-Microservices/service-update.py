from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():

    item = request.form.get('item')
    name = request.form.get('name')
    category = request.form.get('category')

    _item = us.item()
    data = [x for x in _item if x["item"]==item]
    
    if not data:
        return {"error": "Item not found"}, 401

    item = request.form.get('item')
    passwd = request.form.get('password')
    name = request.form.get('name')

    if item:
        data['item'] = item
    if passwd:
        data['name'] = name
    if name :
        data['category'] = category

    return {"message": "Item updated successfully"}, 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) #127.0.0.1