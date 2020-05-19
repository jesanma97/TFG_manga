from flask import Flask,request,jsonify,abort
from flask_restful import Resource, Api
from json import dumps
#import jsonify
import mysql.connector

try:
    conn = mysql.connector.connect(host="localhost",port=3306,db="mydb",user="root",password="")
    cursor = conn.cursor()
    app = Flask(__name__)
    api = Api(app)
    app.config['JSON_AS_ASCII'] = False

    class Coleccion(Resource):
        def get(self):
            cursor.execute("SELECT * FROM `colección`")
            query = cursor.fetchall()
            lista = []
            for x in query:
                dictionary = {}
                dictionary['titulo'] = x[0]
                dictionary['titulo_original'] = x[1]
                dictionary['dibujante'] = x[2]
                dictionary['guionista'] = x[3]
                dictionary['editorial_francesa'] = x[4]
                dictionary['editorial_americana'] = x[5]
                dictionary['editorial_japonesa'] = x[6]
                dictionary['editorial_española'] = x[7]
                dictionary['genero'] = x[8]
                dictionary['formato'] = x[9]
                dictionary['sentido_lectura'] = x[10]
                dictionary['tomos_japon'] = x[11]
                dictionary['tomos_españa'] = x[12]
                lista.append(dictionary)
            return (jsonify(lista))

    
    class Tomo(Resource):
        def get(self):
            cursor.execute("SELECT * FROM `tomos`")
            query = cursor.fetchall()
            lista = []
            for x in query:
                dictionary = {}
                dictionary['id'] = x[0]
                dictionary['coleccion'] = x[1]
                dictionary['portada'] = x[2]
                dictionary['titulo'] = x[3]
                dictionary['paginas'] = x[4]
                dictionary['precio'] = x[5]
                lista.append(dictionary)
            return (jsonify(lista))


    class Novedad(Resource):
        def get(self):
            cursor.execute("SELECT * FROM `novedades`")
            query = cursor.fetchall()
            lista = []
            for x in query:
                dictionary = {}
                dictionary['fecha'] = x[1]
                dictionary['portada'] = x[2]
                dictionary['tomo'] = x[3]
                lista.append(dictionary)
            return (jsonify(lista))
    
    class Coleccion_Ind(Resource):
        def get(self,titulo_colec):
            cursor.execute("SELECT * FROM `colección`")
            query = cursor.fetchall()
            lista = []
            lista2 = []
            for x in query:
                dictionary = {}
                dictionary['titulo'] = x[0]
                dictionary['titulo_original'] = x[1]
                dictionary['dibujante'] = x[2]
                dictionary['guionista'] = x[3]
                dictionary['editorial_francesa'] = x[4]
                dictionary['editorial_americana'] = x[5]
                dictionary['editorial_japonesa'] = x[6]
                dictionary['editorial_española'] = x[7]
                dictionary['genero'] = x[8]
                dictionary['formato'] = x[9]
                dictionary['sentido_lectura'] = x[10]
                dictionary['tomos_japon'] = x[11]
                dictionary['tomos_españa'] = x[12]
                lista.append(dictionary)
            for x in lista:
                print(x['dibujante'])
            task = [task for task in lista if task['titulo'] == titulo_colec]
            if len(task) == 0:
                abort(404)
            return (jsonify(task[0]))

    class Dibujante(Resource):
        def get(self,dibujantes):
            cursor.execute("SELECT * FROM `colección`")
            query = cursor.fetchall()
            lista = []
            lista2 = []
            for x in query:
                dictionary = {}
                dictionary['titulo'] = x[0]
                dictionary['titulo_original'] = x[1]
                dictionary['dibujante'] = x[2]
                dictionary['guionista'] = x[3]
                dictionary['editorial_francesa'] = x[4]
                dictionary['editorial_americana'] = x[5]
                dictionary['editorial_japonesa'] = x[6]
                dictionary['editorial_española'] = x[7]
                dictionary['genero'] = x[8]
                dictionary['formato'] = x[9]
                dictionary['sentido_lectura'] = x[10]
                dictionary['tomos_japon'] = x[11]
                dictionary['tomos_españa'] = x[12]
                lista.append(dictionary)
            task = [task for task in lista if task['dibujante'] == dibujantes]
            if len(task) == 0:
                abort(404)
            return (jsonify(task))
    
    class Guionista(Resource):
        def get(self,guionistas):
            cursor.execute("SELECT * FROM `colección`")
            query = cursor.fetchall()
            lista = []
            lista2 = []
            for x in query:
                dictionary = {}
                dictionary['titulo'] = x[0]
                dictionary['titulo_original'] = x[1]
                dictionary['dibujante'] = x[2]
                dictionary['guionista'] = x[3]
                dictionary['editorial_francesa'] = x[4]
                dictionary['editorial_americana'] = x[5]
                dictionary['editorial_japonesa'] = x[6]
                dictionary['editorial_española'] = x[7]
                dictionary['genero'] = x[8]
                dictionary['formato'] = x[9]
                dictionary['sentido_lectura'] = x[10]
                dictionary['tomos_japon'] = x[11]
                dictionary['tomos_españa'] = x[12]
                lista.append(dictionary)
            task = [task for task in lista if task['dibujante'] == guionistas]
            task2 = [task for task in lista if task['guionista'] == guionistas]
            if len(task2) == 0:
                abort(404)
            
            if task['dibujante'] == task['guionista']:
                pass
            else:
                return (jsonify(task))

    class Tomo_Colec(Resource):
        def get(self,titulo):
            cursor.execute("SELECT * FROM `tomos`")
            query = cursor.fetchall()
            lista = []
            for x in query:
                dictionary = {}
                dictionary['id'] = x[0]
                dictionary['coleccion'] = x[1]
                dictionary['portada'] = x[2]
                dictionary['titulo'] = x[3]
                dictionary['paginas'] = x[4]
                dictionary['precio'] = x[5]
                lista.append(dictionary)
            task = [task for task in lista if task['coleccion'] == titulo]
            return (jsonify(task))

            
            
            
    api.add_resource(Coleccion, '/api/v1/colecciones', methods=['GET']) #Ruta 1
    api.add_resource(Tomo, '/api/v1/tomos', methods=['GET']) #Ruta 2
    api.add_resource(Novedad, '/api/v1/novedades', methods=['GET']) #Ruta 3 
    api.add_resource(Coleccion_Ind, '/api/v1/colecciones/<string:titulo_colec>', methods=['GET']) #Ruta 4
    api.add_resource(Dibujante, '/api/v1/colecciones/<string:dibujantes>', methods=['GET']) #Ruta 5
    api.add_resource(Guionista, '/api/v1/colecciones/<string:guionistas>', methods=['GET']) #Ruta 6
    api.add_resource(Tomo_Colec, '/api/v1/tomos/<string:titulo>', methods=['GET']) #Ruta 7


    if __name__ == '__main__':
        app.run(port='5002')
except mysql.connector.Error as e:
    print("Failed to insert record into MySQL table {}".format(error))
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
