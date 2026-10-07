from flask import Flask, render_template
from routes.page_routes import page_bp
from routes.api_routes import api_bp
from models.flight_model import create_table
import os
import pickle
import sqlite3
app = Flask(__name__)
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
MODEL_PATH=os.path.join(BASE_DIR,"flight_delay_model.pkl")
model=pickle.load(open(MODEL_PATH,"rb"))
app.config["MODEL"]=model
create_table()
app.register_blueprint(page_bp)
app.register_blueprint(api_bp)
if __name__ == "__main__":
    app.run(debug=True)