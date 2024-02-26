from flask import Blueprint, request, Response, json, render_template, redirect, url_for
from src.services.cliente_service import Clientes_Service
from src.services.musicas_service import Musicas_Favoritas_Service

class Main_Controller(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        self.route("/", methods=["GET"])(self.get_all_data)
        self.route("/clientes/<int:id_cliente>", methods=["GET"])(self.get_cliente_by_id)
        self.route("/musicas/<int:id_musica>", methods=["GET"])(self.get_musica_by_id)
        self.route("/clientes", methods=["POST"])(self.create_cliente)
        self.route("/musicas", methods=["POST"])(self.create_musica)
        self.route("/clientes/create", methods=["GET"])(self.create_cliente_page)
        self.route("/musicas/create", methods=["GET"])(self.create_musica_page)
    
    def get_all_data(self):
        clientes_response, clientes_status_code = Clientes_Service.get_all(html=True)
        musicas_response, musicas_status_code = Musicas_Favoritas_Service.get_all(html=True)

        return render_template('index.html', clients=clientes_response, musicas=musicas_response), 200
    
    def get_cliente_by_id(self, id_cliente):
        response_data, status_code = Clientes_Service.get_by_id(id_cliente)
        return response_data, status_code
    
    def get_musica_by_id(self, id_musica):
        response_data, status_code = Musicas_Favoritas_Service.get_by_id(id_musica)
        return response_data, status_code
    
    def create_cliente(self):
        request_data = request.form

        response_data, status_code = Clientes_Service.create(request_data)
        if status_code == 201:
            return redirect(url_for('.get_all_data'))
        else:
            return response_data, status_code
    
    def create_musica(self):
        request_data = request.form

        response_data, status_code = Musicas_Favoritas_Service.create(request_data)
        if status_code == 201:
            return redirect(url_for('.get_all_data'))
        else:
            return response_data, status_code
        
    def create_cliente_page(self):
        return render_template('create_cliente.html')

    def create_musica_page(self):
        return render_template('create_musica.html')

main_blueprint = Main_Controller("main", __name__)
