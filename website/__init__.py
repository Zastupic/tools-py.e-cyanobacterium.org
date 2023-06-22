from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tif', 'tiff', 'gif', 'bmp'}

images = UploadSet("images", IMAGES)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'blablabla' 
    app.config["UPLOADED_IMAGES_DEST"] = UPLOAD_FOLDER
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) 

    from .views import views
    from .auth import auth
    from .cell_count import cell_count
    from .clear_uploads import clear_uploads

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(cell_count, url_prefix='/')
    app.register_blueprint(clear_uploads, url_prefix='/')

    from .models import User

    #### DATABASE ####
    with app.app_context(): # creating the database
        db.create_all()

    #### LOGIN MANAGAER ####
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # where flask will redirect user when not logged in
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    #### UPLOADING IMAGE ####
    configure_uploads(app, images)  

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')