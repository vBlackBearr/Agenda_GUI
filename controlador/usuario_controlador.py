from modelo.usuario import Usuario
import cx_Oracle
from bdd import config

class UsuarioControlador:
    def crear_usuario(self, usuario):
        with cx_Oracle.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO usuarios (id, nombre, correo) VALUES (:id, :nombre, :correo)",
                               id=usuario.id, nombre=usuario.nombre, correo=usuario.correo)
                connection.commit()

    def obtener_usuarios(self):
        usuarios = []
        with cx_Oracle.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, correo FROM usuarios")
                for row in cursor:
                    usuarios.append(Usuario(*row))
        return usuarios

    def actualizar_usuario(self, usuario):
        with cx_Oracle.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE usuarios SET nombre = :nombre, correo = :correo WHERE id = :id",
                               nombre=usuario.nombre, correo=usuario.correo, id=usuario.id)
                connection.commit()

    def eliminar_usuario(self, usuario_id):
        with cx_Oracle.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id = :id", id=usuario_id)
                connection.commit()