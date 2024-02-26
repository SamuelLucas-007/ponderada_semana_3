from src import db
import uuid

class Clientes(db.Model):
  __tablename__ = "clientes"

  id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
  nome = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), nullable=False)

  def __init__(self, nome, email):
    self.nome = nome
    self.email = email
  
  def __repr__(self):
    return f"Nome do cliente: {self.nome}, Email: {self.email}"
  
  def save(self):
    """
    Salva o cliente no banco de dados
    """
    db.session.add(self)
    db.session.commit()

  def update(self, nome=None, email=None):
    """
    Atualiza o cliente no banco de dados
    """
    if nome is not None:
      self.nome = nome
    if email is not None:
      self.email = email

    db.session.commit()

  def delete(self):
    """
    Deleta o cliente do banco de dados
    """
    db.session.delete(self)
    db.session.commit()