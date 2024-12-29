import os
from flask import Flask, render_template
from config.db_config import Config
from models.models import db, Department, Job, Employee

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def home():
    return render_template('main_page.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)