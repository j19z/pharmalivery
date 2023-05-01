class Config:

    #Flask Configuaration Variables
    SECRET_KEY = 'thisisthesecretkey'
    STATIC_FOLDER = 'static' # Este parece no hacer nada.
    TEMPLATES_FOLDER = 'template' # Este parece no hacer nada.
    DEBUG = True
    TESTING = True
    PROPAGATE_EXCEPTIONS = True

    #Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'j19z.python@gmail.com'
    MAIL_PASSWORD = 'jarjbcedbedjhmzs'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    #Database
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://DB_USERNAME:DB_PASSWORD@DB_HOST/DB_NAME'
    
    #Server
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@db/pharmalivery_db'
    #Development
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@localhost/pharmalivery_db'

    PROFILE_PIC_FOLDER = 'static//profile_pics'

    #Other Variables
