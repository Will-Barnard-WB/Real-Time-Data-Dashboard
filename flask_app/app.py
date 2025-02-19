from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

# Database connection details
DB_HOST = os.getenv('DB_HOST', 'db')  # Change if necessary
DB_NAME = os.getenv('DB_NAME', 'postgres')
DB_USER = os.getenv('DB_USER', 'airflow')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'airflow')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

@app.route('/')
def home():
    return "Welcome to the home page"



@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM stock_data;')
    stocks = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(stocks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
