from flask import Blueprint, render_template, request, jsonify
from flask_mail import Message
from app import mail, db

main = Blueprint('main', __name__)

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
