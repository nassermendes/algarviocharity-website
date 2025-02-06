from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__, 
                static_folder='../static',
                template_folder='../templates')
    
    app.config.from_object(Config)
    
    db.init_app(app)
    mail.init_app(app)
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app
