from flask import Blueprint
from src.controllers.ponderada_controller import main_blueprint

api = Blueprint("api", __name__)

api.register_blueprint(main_blueprint, url_prefix="/ponderada")
