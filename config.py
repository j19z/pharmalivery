class Config:

    #Flask Configuaration Variables
    SECRET_KEY = 'thisisthesecretkey'
    STATIC_FOLDER = 'static' # Este parece no hacer nada. 
    TEMPLATES_FOLDER = 'template' # Este parece no hacer nada. 
    DEBUG = True
    TESTING = True
    PROPAGATE_EXCEPTIONS = True

    #Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

    PROFILE_PIC_FOLDER = 'static\\profile_pics'
    
    # Other Variables