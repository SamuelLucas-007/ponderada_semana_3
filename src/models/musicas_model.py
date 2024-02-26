from src import db
import uuid

class Musicas_Favoritas(db.Model):
    __tablename__ = "musicas_favoritas"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    artista = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=True)
    usuario_id = db.Column(db.String(36), db.ForeignKey('clientes.id'), nullable=False)
    usuario = db.relationship('Clientes', backref=db.backref('musicas_favoritas', lazy=True))

    def __init__(self, titulo, artista, genero, usuario_id):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.usuario_id = usuario_id

    def __repr__(self):
        return f"Título: {self.titulo}, Artista: {self.artista}, Gênero: {self.genero}, ID do Usuário: {self.usuario_id}"
    
    def save(self):
        """
        Salva a música favorita no banco de dados
        """
        db.session.add(self)
        db.session.commit()

    def update(self, titulo=None, artista=None, genero=None):
        """
        Atualiza a música favorita no banco de dados
        """
        if titulo is not None:
            self.titulo = titulo
        if artista is not None:
            self.artista = artista
        if genero is not None:
            self.genero = genero

        db.session.commit()

    def delete(self):
        """
        Deleta a música favorita do banco de dados
        """
        db.session.delete(self)
        db.session.commit()
