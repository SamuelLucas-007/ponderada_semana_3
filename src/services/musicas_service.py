from src.models.musicas_model import Musicas_Favoritas as MusicasModel
from src.utils import Logging

logger = Logging()

class Musicas_Favoritas_Service:
    @staticmethod
    def get_all(html=False):
        try:
            musicas = MusicasModel.query.all()

            logger.log_info(f'Músicas retornadas com sucesso: {musicas}')

            # Se existem músicas
            if musicas:
                # Se a solicitação é para HTML, renderiza o template com os dados das músicas
                if html:
                    return musicas, 200
                else:
                    # Cria lista de músicas em formato JSON
                    musicas_list = []
                    for musica in musicas:
                        musicas_list.append({
                            'id': musica.id,
                            'titulo': musica.titulo,
                            'artista': musica.artista,
                            'genero': musica.genero,
                            'usuario_id': musica.usuario_id
                        })
                    return {"status": "success", "data": musicas_list}, 200
            else:
                # Se não existem músicas
                if html:
                    return "Músicas não encontradas", 404
                else:
                    return {"status": "failed", "data": "Músicas não encontradas"}, 404
        except Exception as e:
            logger.log_error(f'Erro ao retornar músicas: {e}')
            if html:
                return "Ocorreu um erro", 500
            else:
                return {"status": "failed", "message": "Ocorreu um erro", "error": str(e)}, 500
    
    @staticmethod
    def get_by_id(id):
        try:
            musica = MusicasModel.query.filter_by(id=id).first()
            
            logger.log_info(f'Música retornada com sucesso: {musica}')

            if musica:
                return {"status": "success", "data": {
                    'id': musica.id,
                    'titulo': musica.titulo,
                    'artista': musica.artista,
                    'genero': musica.genero,
                    'usuario_id': musica.usuario_id
                }}, 200
            else:
                return {"status": "failed", "data": "Música não encontrada"}, 404
        except Exception as e:
            logger.log_error(f'Erro ao retornar música: {e}')
            return {"status": "failed", "message": "Ocorreu um erro", "error": str(e)}, 500
    
    @staticmethod
    def create(musica_data):
        try:
            # Criando uma nova música favorita
            new_musica = MusicasModel(
                titulo=musica_data["titulo"],
                artista=musica_data["artista"],
                genero=musica_data["genero"],
                usuario_id=musica_data["usuario_id"]
            )

            new_musica.save()

            logger.log_info(f"Música favorita criada com sucesso: {new_musica}")

            return {"status": "success", "message": "Música favorita criada com sucesso", "data": musica_data}, 201
        except Exception as e:
            return {"status": "failed", "message": "Ocorreu um erro", "error": str(e)}, 500
