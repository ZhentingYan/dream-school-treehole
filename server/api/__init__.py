from . import post, user, comment


def init_app(app):
    app.register_blueprint(post.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(comment.bp)
