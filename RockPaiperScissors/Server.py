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

engine = create_engine(r'sqlite:///C:\Users\pjene\Desktop\Schule\Anichstraße-HTL\5.AHWII\Cloud-Computing\File-Server-11\imageServer.sqlite3') #Welche Datenbank wird verwendet
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
Base.query = db_session.query_property() #Dadurch hat jedes Base - Objekt (also auch ein GeoInfo) ein Attribut query für Abfragen
app = Flask(__name__) #Die Flask-Anwendung
api = Api(app) #Die Flask API

@dataclass #Diese ermoeglicht das Schreiben als JSON mit jsonify
class BinaryWithMetadata(Base):
    __tablename__ = 'images'  # Abbildung auf diese Tabelle
    id: int
    name: str
    ext: str
    data: str
    desc : str
    when: str
    descT : str
    descAna : str

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    ext = Column(Text)
    data = Column(Text)
    desc = Column(Text)
    when = Column(DateTime, default=func.now())
    descT = Column(Text)
    descAna = Column(Text)


class BinaryWithMetadataREST(Resource):
    def get(self, id):
        infos = BinaryWithMetadata.query.get(id)
        return jsonify(infos)

    def put(self,id):
        d = request.get_json(force=True)
        s = translate(d['desc'])
        ds = analyzeIMG(d['data'])
        print(ds)
        info = BinaryWithMetadata(name=d['name'], ext=d['ext'], data=d['data'], desc=d['desc'], descT=s, descAna = ds)
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
api.add_resource(BinaryWithMetadataREST, '/img_meta/<int:id>')


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

# Wenn Logging-Information fuer den Client vorhanden ist (gut fuer das Fehlersuchen)
def on_log(client, userdata, level, buf):
    print("log: ",buf)

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

@app.route("/getLastImage")
def get_last_image():
    res = BinaryWithMetadata.query.all()
    #todo get last image

@app.route("/search/<string:data>")
def search(data):
    res = BinaryWithMetadata.query.filter(or_(BinaryWithMetadata.name.contains(data),BinaryWithMetadata.desc.contains(data))).all()
    print(res)
    return jsonify(res)
 
@app.teardown_appcontext
def shutdown_session(exception=None):
    print("Shutdown Session")
    db_session.remove()

def init_db():
    # Erzeugen der Tabellen für die Klassen, die oben deklariert sind (muss nicht sein, wenn diese schon existiert)
    Base.metadata.create_all(bind=engine)

def startPicture():
    client = mqtt.Client('Server')  # Der Parameter ist die client-ID, diese sollte möglichst eindeutig sein.
    client.username_pw_set('patrick', 'patrick')
    client.connect('192.168.10.100', port=2222)   # Im Moment verwenden wir die lokale mosquitto Installation, spaeter durch die IP zu ersetzen
    client.publish("take/picture","TAKE")
    print("Publishing")

if __name__ == '__main__':
    init_db()
    #startPicture()
    app.run()
    #app.run(host='192.168.10.100', port=81)
    
    