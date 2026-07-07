from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        port=os.environ.get('DB_PORT'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME')
    )
    return conn

@app.route('/')
def home():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT NOW()')
        time = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return jsonify({
            'message': 'App is running!',
            'time': str(time),
            'database': 'Connected to PostgreSQL ✅'
        })
    except Exception as e:
        return jsonify({
            'message': 'Database not connected ❌',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)