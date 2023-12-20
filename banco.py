import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Double

#cria a engine e conecta ao banco de dados
engine = sqlalchemy.create_engine('sqlite:///banco.db', echo=True)

# cria a classe base para as declarações da tabela
Base = declarative_base()

#define a classe do modelo (tabela)
class Item(Base):
    __tablename__ = 'itens'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    ITEM = Column(String(50))
    VALOR = Column(Double)

    def __repr__(self):
        return '<Item(ITEM=%s, VALOR=%s)>' % (self.ITEM, self.VALOR)
    
#cria a tabela no banco de dados
Base.metadata.create_all(engine)

#cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

#define os métodos de inserção, leitura e exclusão
def inserir_item(item, valor):
    novo_item = Item(ITEM=item, VALOR=valor)
    session.add(novo_item)
    session.commit()

def listar_itens():
    import pandas as pd
    itens = session.query(Item).all()
    lista = []
    for item in itens:
        lista.append([item.ID, item.ITEM, item.VALOR])
    lista = pd.DataFrame(lista, columns=['ID', 'ITEM', 'VALOR'])
    return lista

def excluir_item(item_id):
    item = session.query(Item).filter_by(ID=item_id).first()
    if item:
        session.delete(item)
        session.commit()
        print(f'Item com ID {item_id} excluído com sucesso!')
    else:
        print(f'Item com ID {item_id} não encontrada.')

