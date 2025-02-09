from flask import Flask, render_template, redirect, request, url_for, send_from_directory
from flask_talisman import Talisman
import os
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')
Talisman(app, force_https=True)

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
