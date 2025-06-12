from flaskapp.config import Config
from flask import Flask, redirect, url_for


def create_app(config_class=Config):
  app: Flask = Flask(__name__)
  app.config.from_object(config_class)

  @app.errorhandler(404)
  def not_found(e):
    return redirect(url_for("core.index"))

  # Importing Blueprints
  from flaskapp.core.routes import core

  # Registering Blueprints
  app.register_blueprint(core, url_prefix="/")

  return app
