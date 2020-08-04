from flask import Flask, render_template
from flask_cors import CORS


def create_app():

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    CORS(app, supports_credentials=True)

    import db
    import auth  # , api

    db.init_app(app)
    # api.init_app(app)
    app.register_blueprint(auth.bp)

    return app


if __name__ == "__main__":

    app = create_app()
    app.secret_key = 'dev'
    app.env = 'development'
    app.debug = True

    app.run(host='127.0.0.1', port=8000)
