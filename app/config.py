class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{pass}@{host}/{dbname}?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = ''


Config = DevelopmentConfig