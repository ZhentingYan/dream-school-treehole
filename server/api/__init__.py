from . import post, user


def init_app(app):
    app.register_blueprint(post.bp)
    app.register_blueprint(user.bp)
