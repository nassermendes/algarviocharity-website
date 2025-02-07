from flask import Blueprint, render_template, request, jsonify, send_from_directory
from flask_mail import Message
from app import mail, db
from datetime import datetime

main = Blueprint('main', __name__)

@main.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/projects')
def projects():
    return render_template('projects.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.get_json()
        
        msg = Message('New Contact Form Submission',
                     sender=data['email'],
                     recipients=['contact@algarviocharity.org'])
        
        msg.body = f"""
        Name: {data['name']}
        Email: {data['email']}
        Message: {data['message']}
        """
        
        try:
            mail.send(msg)
            return jsonify({'status': 'success'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500
            
    return render_template('contact.html')

@main.route('/donate')
def donate():
    return render_template('donate.html')

@main.route('/.well-known/acme-challenge/TYKjpIhVL-t2ifwPKMs_HfER7VBl5uP_HgYfBNqEC8qk0nqPphIP3MU50TVDLLDY')
def acme_challenge():
    return send_from_directory('.well-known/acme-challenge', 'TYKjpIhVL-t2ifwPKMs_HfER7VBl5uP_HgYfBNqEC8qk0nqPphIP3MU50TVDLLDY')
