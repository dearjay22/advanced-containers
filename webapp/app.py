from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Database connection
db_config = {
    'host': os.environ.get('DB_HOST', 'db'),
    'user': os.environ.get('DB_USER', 'user'),
    'password': os.environ.get('DB_PASSWORD', 'password'),
    'database': os.environ.get('DB_NAME', 'userdata')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (first_name, last_name) VALUES (%s, %s)",
        (data['first_name'], data['last_name'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'status': 'success'}), 201

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
