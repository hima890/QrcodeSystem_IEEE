from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from config import Config
import os
# from flask_whooshalchemy import whoosh


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
mail = Mail()


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#the main app function
def create_app(config_class=Config):
    # the Flask class instaince 
    app = Flask(__name__)
    # import the configration from config file
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    mail.init_app(app)
    # whoosh.init_app(app)
    # create the database
    with app.app_context():
        import models
        db.create_all()
        
    # register the main blueprint
    from theFormForaccepted.form.routes import home_page
    from theFormForaccepted.errors.routes import errors

    app.register_blueprint(home_page)
    # app.register_blueprint(errors)
    return app