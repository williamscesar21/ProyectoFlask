from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

mysql = MySQL(app)

#----------------------------------------- METODOS GET PARA CADA TABLA --------------------------------------

#--------- METODO GET LIBROS-----

@app.route('/libreria/libros', methods=['GET'])
def visualizarlibros():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM libros")
    columnas = [columna[0] for columna in cursor.description]
    libros = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    res = jsonify(libros)
    res.headers.add("Acces-Control-Allow-Origin","*")
    return res

@app.route('/libreria/libros/<id>', methods=['GET'])
def visualizarLibroId(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM libros WHERE id = %s", (id,))
    columnas = [columna[0] for columna in cursor.description]
    libro_data = cursor.fetchone()
    cursor.close()

    if libro_data:
        libro = dict(zip(columnas, libro_data))
        return jsonify(libro)
    else:
        return jsonify({"resultado": "El libro no fue encontrado"}), 404
    
#-------------- METODO GET USUARIOS-------

@app.route('/libreria/usuarios', methods=['GET'])
def visualizarusuarios():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    res = jsonify(usuarios)
    res.headers.add("Acces-Control-Allow-Origin","*")
    return res

@app.route('/libreria/usuarios/<id>', methods=['GET'])
def visualizarUsuarioId(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    res = cursor.fetchone()
    cursor.close()
    
    if res:
        return jsonify(res)
    else:
        return jsonify({"resultado":"El usuario no fue encontrado"}), 404
    
#----------- METODO GET GENEROS

@app.route('/libreria/generos', methods=['GET'])
def visualizargeneros():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM generos")
    generos = cursor.fetchall()
    cursor.close()
    res = jsonify(generos)
    res.headers.add("Acces-Control-Allow-Origin","*")
    return res

@app.route('/libreria/generos/<id>', methods=['GET'])
def visualizarGeneroId(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM generos WHERE id = %s", (id,))
    res = cursor.fetchone()
    cursor.close()
    
    if res:
        return jsonify(res)
    else:
        return jsonify({"resultado":"El genero no fue encontrado"}), 404
    
#---------- METODO GET AUTORES
    
@app.route('/libreria/autores', methods=['GET'])
def visualizarautores():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM autores")
    autores = cursor.fetchall()
    cursor.close()
    res = jsonify(autores)
    res.headers.add("Acces-Control-Allow-Origin","*")
    return res

@app.route('/libreria/autores/<id>', methods=['GET'])
def visualizarAutorId(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM autores WHERE id = %s", (id,))
    res = cursor.fetchone()
    cursor.close()
    
    if res:
        return jsonify(res)
    else:
        return jsonify({"resultado":"El usuario no fue encontrado"}), 404
    
#--------- METODO GET EDITORIALES
    
@app.route('/libreria/editoriales', methods=['GET'])
def visualizareditoriales():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM editoriales")
    editoriales = cursor.fetchall()
    cursor.close()
    res = jsonify(editoriales)
    res.headers.add("Acces-Control-Allow-Origin","*")
    return res

@app.route('/libreria/editoriales/<id>', methods=['GET'])
def visualizarEditorialId(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM editoriales WHERE id = %s", (id,))
    res = cursor.fetchone()
    cursor.close()
    
    if res:
        return jsonify(res)
    else:
        return jsonify({"resultado":"El usuario no fue encontrado"}), 404
    
#--------- METODO GET RESEÑAS

@app.route('/libreria/reseñas', methods=['GET'])
def visualizarreseñas():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM reseñas")
    reseñas = cursor.fetchall()
    cursor.close()
    res = jsonify(reseñas)
    res.headers.add("Acces-Control-Allow-Origin","*")
    return res

@app.route('/libreria/reseñas/<id>', methods=['GET'])
def visualizarResennaId(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM reseñas WHERE id = %s", (id,))
    res = cursor.fetchone()
    cursor.close()
    
    if res:
        return jsonify(res)
    else:
        return jsonify({"resultado":"El usuario no fue encontrado"}), 404
    

    
#---------------------------------- METODO POST PARA TODAS LAS TABLAS ----------------------------------------
    
#-------- METODO POST PARA LIBROS

@app.route('/libreria/aggLibros', methods = ['POST'] )
def agregarLibros():     
    titulo = request.json['titulo']
    anno_publicacion = request.json['anno_publicacion']
    autor_id = request.json['autor_id']
    genero_id = request.json['genero_id']
    editorial_id = request.json['editorial_id']

    cursor = mysql.connection.cursor()
    cursor.execute('USE libreria')
    cursor.execute('INSERT INTO libros ( titulo, anno_publicacion, autor_id, genero_id, editorial_id) VALUES( %s, %s, %s, %s, %s)', ( titulo, anno_publicacion, autor_id, genero_id, editorial_id))
    mysql.connection.commit() 
    cursor.close() 
    return jsonify({"mensaje":"Libro agregado exitosamente"})


    
#-------- METODO POST PARA AUTORES

@app.route('/libreria/aggAutores', methods = ['POST'] )
def agregarAutores():   
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute('USE libreria')
    cursor.execute('INSERT INTO autores (nombre) VALUES (%s)', (nombre,))
    mysql.connection.commit() 
    cursor.close() 
    return jsonify({"mensaje":"Autor agregado exitosamente"})


#-------- METODO POST PARA GENEROS

@app.route('/libreria/aggGeneros', methods = ['POST'] )
def agregarGeneros():   
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute('USE libreria')
    cursor.execute('INSERT INTO generos (nombre) VALUES(%s)', (nombre,))
    mysql.connection.commit() 
    cursor.close() 
    return jsonify({"mensaje":"Genero agregado exitosamente"})


#-------- METODO POST PARA EDITORIALES

@app.route('/libreria/aggEditoriales', methods = ['POST'] )
def agregarEditoriales():   
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute('USE libreria')
    cursor.execute('INSERT INTO editoriales (nombre) VALUES(%s)', (nombre,))
    mysql.connection.commit() 
    cursor.close() 
    return jsonify({"mensaje":"Editorial agregada exitosamente"})


#-------- METODO POST PARA RESEÑAS

@app.route('/libreria/aggResenna', methods = ['POST'] )
def agregarReseña():   
    contenido = request.json['contenido']
    libro_id = request.json['libro_id']
    usuario_id = request.json['usuario_id']

    cursor = mysql.connection.cursor()
    cursor.execute('USE libreria')
    cursor.execute('INSERT INTO reseñas (id, contenido, libro_id, usuario_id) VALUES(%s, %s, %s, %s)', (id, contenido, libro_id, usuario_id))
    mysql.connection.commit() 
    cursor.close() 
    return jsonify({"mensaje":"Reseña agregada exitosamente"})



#-------- METODO POST PARA USUARIOS

@app.route('/libreria/aggUsuarios', methods = ['POST'] )
def agregarUsuario():   
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute('USE libreria')
    cursor.execute('INSERT INTO usuarios (nombre) VALUES(%s)', (nombre,))
    mysql.connection.commit() 
    cursor.close() 
    return jsonify({"mensaje":"Usuario agregado exitosamente"})


#---------------------------------- METODO DELETE PARA TODAS LAS TABLAS ----------------------------------------

#---------------- METODO DELETE LIBROS

@app.route('/libreria/eliminarLibro/<id>', methods=['DELETE'])
def eliminarLibro21(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    cursor.execute("DELETE FROM libros WHERE id = %s", (id))
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':"Se elimino  el libro"})


#---------------- METODO DELETE AUTORES

@app.route('/libreria/eliminarAutor/<id>', methods=['DELETE'])
def eliminarAutor(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    cursor.execute("DELETE FROM autores WHERE id = %s", (id))
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':"Se elimino  el autor"})

#---------------- METODO DELETE GENEROS

@app.route('/libreria/eliminarGenero/<id>', methods=['DELETE'])
def eliminarGenero(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    cursor.execute("DELETE FROM generos WHERE id = %s", (id))
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':"Se elimino  el genero"})


#---------------- METODO DELETE EDITORIALES

@app.route('/libreria/eliminarEditorial/<id>', methods=['DELETE'])
def eliminarEditorial(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    cursor.execute("DELETE FROM editoriales WHERE id = %s", (id))
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':"Se elimino  la editorial"})


#---------------- METODO DELETE RESEÑAS

@app.route('/libreria/eliminarResenna/<id>', methods=['DELETE'])
def eliminarResenna(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    cursor.execute("DELETE FROM reseñas WHERE id = %s", (id))
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':"Se elimino  la reseña"})


#---------------- METODO DELETE USUARIOS

@app.route('/libreria/eliminarUsuario/<id>', methods=['DELETE'])
def eliminarUsuario(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id))
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    mysql.connection.commit()
    cursor.close()
    return jsonify({'resultado':"Se elimino  el usuario"})



#---------------------------------- METODO PATCH PARA TODAS LAS TABLAS ----------------------------------------

#---------------- METODO PATCH LIBROS

@app.route("/libreria/editarLibro/<id>", methods=["PATCH"])
def actualizar_libro(id):
    datos_actualizados = request.json
    if not datos_actualizados:
        return jsonify({'error':'No se enviaron datos'})
    cursor = mysql.connection.cursor()
    update_query = "UPDATE libros SET "
    update_data = []
    for campo, valor in datos_actualizados.items():
        if campo in ["titulo", "anno_publicacion", "autor_id","genero_id", "editorial_id"]:
            update_query += f"{campo} = %s, "
            update_data.append(valor)
    
    if not update_data:
        return jsonify({"error":"Los datos estan vacios"})
    update_query = update_query.rstrip(', ')
    update_query += " WHERE id = %s"
    update_data.append(id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'resultado':'Informacion actualizada correctamente'})



#---------------- METODO PATCH AUTORES

@app.route("/libreria/editarAutor/<id>", methods=["PATCH"])
def actualizar_autor(id):
    datos_actualizados = request.json
    if not datos_actualizados:
        return jsonify({'error':'No se enviaron datos'})
    cursor = mysql.connection.cursor()
    update_query = "UPDATE autores SET "
    update_data = []
    for campo, valor in datos_actualizados.items():
        if campo in ["nombre"]:
            update_query += f"{campo} = %s, "
            update_data.append(valor)
    
    if not update_data:
        return jsonify({"error":"Los datos estan vacios"})
    update_query = update_query.rstrip(', ')
    update_query += " WHERE id = %s"
    update_data.append(id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'resultado':'Informacion actualizada correctamente'})



#---------------- METODO PATCH GENEROS

@app.route("/libreria/editarGenero/<id>", methods=["PATCH"])
def actualizar_genero(id):
    datos_actualizados = request.json
    if not datos_actualizados:
        return jsonify({'error':'No se enviaron datos'})
    cursor = mysql.connection.cursor()
    update_query = "UPDATE generos SET "
    update_data = []
    for campo, valor in datos_actualizados.items():
        if campo in ["nombre"]:
            update_query += f"{campo} = %s, "
            update_data.append(valor)
    
    if not update_data:
        return jsonify({"error":"Los datos estan vacios"})
    update_query = update_query.rstrip(', ')
    update_query += " WHERE id = %s"
    update_data.append(id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'resultado':'Informacion actualizada correctamente'})



#---------------- METODO PATCH EDITORIALES

@app.route("/libreria/editarEditorial/<id>", methods=["PATCH"])
def actualizar_editorial(id):
    datos_actualizados = request.json
    if not datos_actualizados:
        return jsonify({'error':'No se enviaron datos'})
    cursor = mysql.connection.cursor()
    update_query = "UPDATE editoriales SET "
    update_data = []
    for campo, valor in datos_actualizados.items():
        if campo in ["nombre"]:
            update_query += f"{campo} = %s, "
            update_data.append(valor)
    
    if not update_data:
        return jsonify({"error":"Los datos estan vacios"})
    update_query = update_query.rstrip(', ')
    update_query += " WHERE id = %s"
    update_data.append(id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'resultado':'Informacion actualizada correctamente'})



#---------------- METODO PATCH RESEÑAS

@app.route("/libreria/editarResenna/<id>", methods=["PATCH"])
def actualizar_reseña(id):
    datos_actualizados = request.json
    if not datos_actualizados:
        return jsonify({'error':'No se enviaron datos'})
    cursor = mysql.connection.cursor()
    update_query = "UPDATE reseñas SET "
    update_data = []
    for campo, valor in datos_actualizados.items():
        if campo in ["contenido","libro_id","usuario_id"]:
            update_query += f"{campo} = %s, "
            update_data.append(valor)
    
    if not update_data:
        return jsonify({"error":"Los datos estan vacios"})
    update_query = update_query.rstrip(', ')
    update_query += " WHERE id = %s"
    update_data.append(id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'resultado':'Informacion actualizada correctamente'})


#---------------- METODO PATCH USUARIOS

@app.route("/libreria/editarUsuario/<id>", methods=["PATCH"])
def actualizar_usuario(id):
    datos_actualizados = request.json
    if not datos_actualizados:
        return jsonify({'error':'No se enviaron datos'})
    cursor = mysql.connection.cursor()
    update_query = "UPDATE usuarios SET "
    update_data = []
    for campo, valor in datos_actualizados.items():
        if campo in ["nombre","apellido"]:
            update_query += f"{campo} = %s, "
            update_data.append(valor)
    
    if not update_data:
        return jsonify({"error":"Los datos estan vacios"})
    update_query = update_query.rstrip(', ')
    update_query += " WHERE id = %s"
    update_data.append(id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'resultado':'Informacion actualizada correctamente'})



#----------------------------------------- METODO GET CASO ESPECIAL --------------------------------------

@app.route("/libreria/verLibros", methods=["GET"])
def visualizarlibros2():
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT 
            libros.id AS 'Id_del_libro',
            libros.titulo AS 'Nombre_del_libro',
            autores.nombre AS 'Nombre_del_autor',
            generos.nombre AS 'Nombre_del_genero',
            reseñas.contenido AS 'Texto_de_la_reseña',
            usuarios.nombre AS 'Usuario_de_la_reseña'
        FROM 
            libros
        LEFT JOIN autores ON libros.autor_id = autores.id
        LEFT JOIN generos ON libros.genero_id = generos.id
        LEFT JOIN reseñas ON libros.id = reseñas.libro_id
        LEFT JOIN usuarios ON reseñas.usuario_id = usuarios.id
    """)
    columnas = [columna[0] for columna in cursor.description]
    libros = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    res = jsonify(libros)  
    cursor.close()
    
    if res:
        return res
    else:
        return jsonify({"resultado": "El libro no fue encontrado"}), 404


@app.route("/libreria/verLibro/<id>", methods=["GET"])
def visualizarlibros3(id):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT 
            libros.id AS 'Id del libro',
            libros.titulo AS 'Nombre del libro',
            autores.nombre AS 'Nombre del autor',
            generos.nombre AS 'Nombre del género',
            reseñas.contenido AS 'Texto de la reseña',
            usuarios.nombre AS 'Usuario que realizó la reseña'
        FROM 
            libros
        LEFT JOIN autores ON libros.autor_id = autores.id
        LEFT JOIN generos ON libros.genero_id = generos.id
        LEFT JOIN reseñas ON libros.id = reseñas.libro_id
        LEFT JOIN usuarios ON reseñas.usuario_id = usuarios.id
        WHERE 
            libros.id = %s
    """,(id))

    res = cursor.fetchone()
    cursor.close()
    
    if res:
        return jsonify(res)
    else:
        return jsonify({"resultado":"El libro no fue encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=9090)




