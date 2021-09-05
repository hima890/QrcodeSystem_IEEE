# the configration for databas path and the screet kay
import os


class Config:
    SECRET_KEY = "INDF87fdff"
    SQLALCHEMY_DATABASE_URI =  os.environ['DATABASE_URL']
    MYSQL_DATABASE_CHARSET = 'utf8mb4'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_DEFAULT_SENDER = "IEEENB@gmail.com"
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    MAIL_PORT = 587
    MAIL_USE_TLS = True
  