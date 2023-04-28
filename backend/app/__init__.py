from flask import Flask, render_template
from app.extensions import db, bcrypt, login_manager


def create_app():
    
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

	###################
	### blueprints ####
	###################

    from app.mod_main.views import main as main_blueprint
    from app.mod_user.views import auth as auth_blueprint
    from app.mod_test.views import test as test_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(test_blueprint)
    
    ###################
    ### flask-login ###
    ###################

    login_manager.login_view = 'auth.login'

    from app.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    ########################
	#### error handlers ####
	########################

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/403.html"), 403


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404


    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/500.html", error = error), 500


    ####################
	#### restart db ####
	####################

    with app.app_context():
        db.drop_all()
        db.create_all()


    return app

