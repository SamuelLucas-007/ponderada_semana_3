from src import db
import uuid
from sqlalchemy import DateTime, Float

class Musicas_Favoritas(db.Model):
    __tablename__ = "musicas_favoritas"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    artista = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=True)
    tempo_aproximado = db.Column(db.Float, nullable=True)
    data_lancamento = db.Column(db.DateTime, nullable=True)
    usuario_id = db.Column(db.String(36), db.ForeignKey('clientes.id'), nullable=False)
    usuario = db.relationship('Clientes', backref=db.backref('musicas_favoritas', lazy=True))

    def __init__(self, titulo, artista, genero, usuario_id, tempo_aproximado=None, data_lancamento=None):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.usuario_id = usuario_id
        self.tempo_aproximado = tempo_aproximado
        self.data_lancamento = data_lancamento

    def __repr__(self):
        return f"Título: {self.titulo}, Artista: {self.artista}, Gênero: {self.genero}, ID do Usuário: {self.usuario_id}, Tempo Aproximado: {self.tempo_aproximado}, Data de Lançamento: {self.data_lancamento}"
    
    def save(self):
        """
        Salva a música favorita no banco de dados
        """
        db.session.add(self)
        db.session.commit()

    def update(self, titulo=None, artista=None, genero=None, tempo_aproximado=None, data_lancamento=None):
        """
        Atualiza a música favorita no banco de dados
        """
        if titulo is not None:
            self.titulo = titulo
        if artista is not None:
            self.artista = artista
        if genero is not None:
            self.genero = genero
        if tempo_aproximado is not None:
            self.tempo_aproximado = tempo_aproximado
        if data_lancamento is not None:
            self.data_lancamento = data_lancamento

        db.session.commit()

    def delete(self):
        """
        Deleta a música favorita do banco de dados
        """
        db.session.delete(self)
        db.session.commit()
