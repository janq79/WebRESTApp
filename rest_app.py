from flask import Flask, request, jsonify
import db_connector

app = Flask(__name__)

@app.route('/users/<int:user_id>', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_user(user_id):
    if request.method == 'POST':
        user_name = request.json.get('user_name')
        if not user_name:
            return jsonify(status="error", reason="user_name not provided"), 400

        try:
            added_user_id = db_connector.add_user(user_id, user_name)
            if added_user_id == user_id:
                return jsonify(status="ok", user_added=user_name), 201
            else:
                return jsonify(status="ok", user_added=user_name,
                               info=f"User ID {user_id} was already taken, user added with ID {added_user_id} instead."), 200
        except Exception as e:
            return jsonify(status="error", reason=str(e)), 500

    elif request.method == 'GET':
        try:
            user_name = db_connector.get_user(user_id)
            if user_name:
                return jsonify(status="ok", user_name=user_name), 200
            else:
                return jsonify(status="error", reason="User not found"), 404
        except Exception as e:
            return jsonify(status="error", reason=str(e)), 500

    elif request.method == 'PUT':
        user_name = request.json.get('user_name')
        if not user_name:
            return jsonify(status="error", reason="user_name not provided"), 400

        try:
            db_connector.update_user(user_id, user_name)
            return jsonify(status="ok", user_updated=user_name), 200
        except Exception as e:
            return jsonify(status="error", reason=str(e)), 500

    elif request.method == 'DELETE':
        try:
            db_connector.delete_user(user_id)
            return jsonify(status="ok", user_deleted=user_id), 200
        except Exception as e:
            return jsonify(status="error", reason=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)