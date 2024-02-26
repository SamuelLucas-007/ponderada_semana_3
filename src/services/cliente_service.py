from src.models.cliente_model import Clientes as ClientesModel
from src.utils import Logging

logger = Logging()

class Clientes_Service:
    @staticmethod
    def get_all(html=False):
        try:
            clientes = ClientesModel.query.all()

            logger.log_info(f'Clientes retornados com sucesso: {clientes}')

            # Se existe clientes
            if clientes:
                # Se a solicitação é para HTML, renderiza o template com os dados dos clientes
                if html:
                    return clientes, 200
                else:
                    # Cria lista de clientes em formato JSON
                    clientes_list = []
                    for cliente in clientes:
                        clientes_list.append({
                            'id': cliente.id,
                            'nome': cliente.nome,
                            'email': cliente.email
                        })
                    return {"status": "success", "data": clientes_list}, 200
            else:
                # Se não existe clientes
                if html:
                    return "Clientes não encontrados", 404
                else:
                    return {"status": "failed", "data": "Clientes não encontrados"}, 404
        except Exception as e:
            logger.log_error(f'Erro ao retornar clientes: {e}')
            if html:
                return "Ocorreu um erro", 500
            else:
                return {"status": "failed", "message": "Ocorreu um erro", "error": str(e)}, 500
    
    @staticmethod
    def get_by_id(id):
        try:
            cliente = ClientesModel.query.filter_by(id=id).first()
            
            logger.log_info(f'Cliente retornado com sucesso: {cliente}')

            if cliente:
                return {"status": "success", "data": {
                    'id': cliente.id,
                    'nome': cliente.nome,
                    'email': cliente.email
                }}, 200
            else:
                return {"status": "failed", "data": "Cliente não encontrado"}, 404
        except Exception as e:
            logger.log_error(f'Erro ao retornar cliente: {e}')
            return {"status": "failed", "message": "Ocorreu um erro", "error": str(e)}, 500
    
    @staticmethod
    def create(cliente_data):
        try:
            # Criando um novo cliente

            new_client = ClientesModel(
                nome=cliente_data["nome"],
                email=cliente_data["email"]
            )

            new_client.save()

            logger.log_info(f"Cliente criado com sucesso: {new_client}")

            return {"status": "success", "message": "Cliente criado com sucesso", "data": cliente_data}, 201
        except Exception as e:
            return {"status": "failed", "message": "Ocorreu um erro", "error": str(e)}, 500
