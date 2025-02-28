from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import psycopg2
import os
from datetime import datetime
import logging

app = Flask(__name__)

CORS(app)


DB_HOST = "postgres"
DB_NAME = "postgres"
DB_USER = "airflow"
DB_PASS = "airflow"

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None


@socketio.on('connect')
def handle_connect():
    print("A client has connected")

    emit('stock_update', {'message': 'Welcome to the stock updates WebSocket!'})


@socketio.on('disconnect')
def handle_disconnect():
    print("A client has disconnected")


@socketio.on('request_stock_data')
def handle_request_stock_data():

    conn = get_db_connection()
    if conn is None:
        emit('stock_update', {'error': "Could not connect to database"})
        return
    
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM stock_data;")
        rows = cur.fetchall()
        
        stocks = []
        for row in rows:
            stock = {"name": row[0].isoformat(), "symbol": row[1], "open": row[2], "close": row[3]}
            stocks.append(stock)
        

        emit('stock_update', {'stocks': stocks})
    except Exception as e:
        emit('stock_update', {'error': f"Error fetching data: {str(e)}"})
    finally:
        cur.close()
        conn.close()


@app.route('/push_update')
def push_update():
    app.logger.info("Recived request to /push_update endpoint.")
 
    handle_request_stock_data()
    return "Update sent to clients"


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5050)
