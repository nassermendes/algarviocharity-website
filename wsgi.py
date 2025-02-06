import sys
import os
from dotenv import load_dotenv

# Add your project directory to the sys.path
project_home = '/home/nassermendes/algarviocharity-website'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Load environment variables
load_dotenv(os.path.join(project_home, '.env'))

# Import your Flask app
from run import app as application
