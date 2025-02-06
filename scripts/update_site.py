import os
import subprocess

def update_site():
    """Update the website by pulling latest changes and reloading the web app."""
    try:
        # Change to the website directory
        os.chdir('/home/nassermendes/algarviocharity-website')
        
        # Pull the latest changes
        subprocess.run(['git', 'pull'], check=True)
        
        print("Successfully pulled latest changes")
        return True
    except Exception as e:
        print(f"Error updating site: {str(e)}")
        return False

if __name__ == "__main__":
    update_site()
