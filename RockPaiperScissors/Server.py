from operator import or_
from flask import Flask, request,jsonify, send_from_directory
from flask_restful import Resource, Api
from sqlalchemy import Column, Integer, Text, Float, DateTime, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func
from flask_restful import Resource, Api
from dataclasses import dataclass
import json

app = Flask(__name__) #Die Flask-Anwendung
api = Api(app) #Die Flask API

Base = declarative_base()  # Basisklasse aller in SQLAlchemy verwendeten Klassen
metadata = Base.metadata

engine = create_engine(r'sqlite:///C:\Users\pjene\Desktop\Schule\Anichstraße-HTL\5AHWII\SWP\RockPaperScissor\server.sqlite3') #Welche Datenbank wird verwendet
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
Base.query = db_session.query_property() #Dadurch hat jedes Base - Objekt (also auch ein GeoInfo) ein Attribut query für Abfragen
app = Flask(__name__) #Die Flask-Anwendung
api = Api(app) #Die Flask API

@dataclass #Diese ermoeglicht das Schreiben als JSON mit jsonify
class BinaryWithMetadata(Base):
    __tablename__ = 'data'  # Abbildung auf diese Tabelle
    id: int
    player_name: str
    chosen_symbols: str
    player_won: int

    id = Column(Integer, primary_key=True)
    player_name = Column(Text)
    chosen_symbols = Column(Text)
    player_won = Column(Integer)


class BinaryWithMetadataREST(Resource):
    def get(self, id):
        infos = BinaryWithMetadata.query.get(id)
        return jsonify(infos)

    def put(self,id):
        d = request.get_json(force=True)
        print(d)
        info = BinaryWithMetadata(player_name = d['player_name'], chosen_symbols = d['chosen_symbols'], player_won = d['player_won'])
        db_session.add(info)
        db_session.flush()
        print('Addes Session')
        return jsonify(info)

    def delete(self,id):
        info = BinaryWithMetadata.query.get(id)
        if info == None:
            return jsonify({'message': 'object with id %d does not exist' % id})
        db_session.delete(info)
        db_session.flush()
        return jsonify({'message': '%d deleted' % id})
api.add_resource(BinaryWithMetadataREST, '/data/<int:id>')
 
@app.teardown_appcontext
def shutdown_session(exception=None):
    print("Shutdown Session")
    db_session.remove()

def init_db():
    # Erzeugen der Tabellen für die Klassen, die oben deklariert sind (muss nicht sein, wenn diese schon existiert)
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
    app.run()
    #app.run(host='192.168.10.100', port=81)
    
    