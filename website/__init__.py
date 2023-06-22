from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES
# needed for database - refering
from os import path

# creating database (as object)
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    # seret key for our app, never to be shown to anybody
    # creating database (as object)
    app.config['SECRET_KEY'] = 'blablabla' 
    app.config["UPLOADED_PHOTOS_DEST"] = "static/img"
    # defining location of database (f'sqlite:///{DB_NAME}) - in website folder (where __init__.py is)
    # f: f-string, 'functional' way of string writing - whatever will be in the {} will be evaluated as string
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initializing database - telling the database that it will be used by our app
    db.init_app(app) 

    # we need to import routes defined elsewhere 
    from .views import views
    from .auth import auth
    from .cell_count import cell_counting
    from .clear_uploads import clear_uploads

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(cell_count, url_prefix='/')
    app.register_blueprint(clear_uploads, url_prefix='/')

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


