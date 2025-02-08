from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    # Try to render index.html from the templates folder; if not available, serve the static file
    if os.path.exists(os.path.join(app.template_folder, 'index.html')):
        return render_template('index.html')
    else:
        return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    # Serve static files, if available, else 404
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    elif os.path.exists(path):
        return send_from_directory('.', path)
    else:
        return "Not Found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
