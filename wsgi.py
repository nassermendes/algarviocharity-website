import os
import sys

# Set environment variables
os.environ['SECRET_KEY'] = 'algarviocharity-secret-key-2025'
os.environ['MAIL_USERNAME'] = 'nassermendes@gmail.com'  # Your email
os.environ['MAIL_PASSWORD'] = 'yriaa fuau pxmz syaz'  # You'll need to generate this in Gmail
os.environ['MAIL_SERVER'] = 'smtp.gmail.com'
os.environ['MAIL_PORT'] = '587'
os.environ['MAIL_USE_TLS'] = 'True'

# Add your project directory to the sys.path
project_home = '/home/nassermendes/algarviocharity-website'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import your Flask app
from run import app
application = app  # This is the WSGI callable
