from flask import Flask, render_template_string
import db_connector

app = Flask(__name__)

@app.route('/users/get_user_data/<int:user_id>', methods=['GET'])
def get_user_name(user_id):
    user_name = db_connector.get_user(user_id)
    if user_name:
        return render_template_string("<H1 id='user'>{{ user_name }}</H1>", user_name=user_name)
    else:
        return render_template_string("<H1 id='error'>No such user: {{ user_id }}</H1>", user_id=user_id)

if __name__ == '__main__':
    app.run(debug=True, port=5001)