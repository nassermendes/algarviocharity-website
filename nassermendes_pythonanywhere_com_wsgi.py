import os
import sys
from scripts.update_site import update_site

# Add your project directory to the sys.path
project_home = '/home/nassermendes/algarviocharity-website'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Load environment variables
from dotenv import load_dotenv
dotenv_path = os.path.join(project_home, '.env')
load_dotenv(dotenv_path)

# Update site on each reload
update_site()

# Import and create the Flask app
from app import create_app
application = create_app()
