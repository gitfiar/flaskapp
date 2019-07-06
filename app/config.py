import os

class Config(object):
    SECRET_KEY = os.urandom (24)
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost:3306/flaskrbac?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

    BOOTSTRAP_SERVE_LOCAL  = True
    SECRET_KEY  = 'any secret string'
    UPLOADED_CSVFILES_DEST  = '/var/uploads'
    UPLOADED_IMAGES_DEST = 'upload_file/'
    # We initialize the navigation as well
    UPLOADED_PHOTOS_DEST  = os.getcwd() + 'upload_file/'
    UPLOAD_FOLDER = 'upload_file/'
    UPLOAD_FOLDER  = UPLOAD_FOLDER
    SQLALCHEMY_DATABASE_URI  ='mysql://root:123456@localhost:3306/flask'
    SQLALCHEMY_COMMIT_TEARDOWN  = True
    SQLALCHEMY_TRACK_MODIFICATIONS  = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN  = True

    @staticmethod
    def init_app(app):
        pass



