from modelo.usuarioBM import Usuario
import cx_Oracle
from bdd import config
from fastapi.responses import JSONResponse

class UsuarioControlador:
    def crear_usuario(self, usuario):
        with cx_Oracle.connect(user=config.user, password=config.password, dsn=config.dsn) as connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO USUARIOS(ID_USUARIO,NOMBRE,APELLIDO_PAT,APELLIDO_MAT,USUARIO_BD,CONTRASENIA_BD,ENDPOINT,DICCIONARIO,USUARIO_AGENDA,CONTRASENIA_AGENDA)VALUES(:ID_USUARIO,:NOMBRE,:APELLIDO_PAT,:APELLIDO_MAT,:USUARIO_BD,:CONTRASENIA_BD,:ENDPOINT,:DICCIONARIO,:USUARIO_AGENDA,:CONTRASENIA_AGENDA)",
                               ID_USUARIO= usuario.ID_USUARIO,NOMBRE= usuario.NOMBRE,APELLIDO_PAT= usuario.APELLIDO_PAT,APELLIDO_MAT= usuario.APELLIDO_MAT,USUARIO_BD= usuario.USUARIO_BD,CONTRASENIA_BD= usuario.CONTRASENIA_BD,ENDPOINT= usuario.ENDPOINT,DICCIONARIO= usuario.DICCIONARIO,USUARIO_AGENDA= usuario.USUARIO_AGENDA,CONTRASENIA_AGENDA= usuario.CONTRASENIA_AGENDA)
                connection.commit()

    def obtener_usuarios(self):
        usuarios = []
        with cx_Oracle.connect(user=config.user, password=config.password, dsn=config.dsn) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios")
                columns = [col[0] for col in cursor.description] 
                for row in cursor:
                    usuario = dict(zip(columns, row))
                    usuarios.append(usuario)
        return JSONResponse(content={"requests": usuarios}, status_code=201)

    def actualizar_usuario(self, usuario):
        with cx_Oracle.connect(user=config.user, password=config.password, dsn=config.dsn) as connection:
            with connection.cursor() as cursor:
                sql_query = f"UPDATE usuarios SET nombre = :nombre, apellido_pat = :apellido_pat, apellido_mat = :apellido_mat, usuario_bd = :usuario_bd, contrasenia_bd = :contrasenia_bd, endpoint = :endpoint, diccionario = :diccionario, usuario_agenda = :usuario_agenda, contrasenia_agenda = :contrasenia_agenda WHERE id_usuario = :id_usuario"
                cursor.execute(sql_query,
                               nombre=usuario.NOMBRE, apellido_pat=usuario.APELLIDO_PAT, apellido_mat=usuario.APELLIDO_MAT, usuario_bd=usuario.USUARIO_BD, contrasenia_bd=usuario.CONTRASENIA_BD, endpoint=usuario.ENDPOINT, diccionario=usuario.DICCIONARIO, usuario_agenda=usuario.USUARIO_AGENDA, contrasenia_agenda=usuario.CONTRASENIA_AGENDA, id_usuario=usuario.ID_USUARIO)
                connection.commit()

    def eliminar_usuario(self, usuario_id):
        with cx_Oracle.connect(user=config.user, password=config.password, dsn=config.dsn) as connection:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios WHERE ID_USUARIO = :id", id=usuario_id)
                connection.commit()

def buscar_usuario_por_credenciales_agenda(self, usuario_agenda, contrasenia_agenda):
        with cx_Oracle.connect(user=config.user, password=config.password, dsn=config.dsn) as connection:
            with connection.cursor() as cursor:
                sql_query = "SELECT * FROM usuarios WHERE USUARIO_AGENDA = :usuario_agenda AND CONTRASENIA_AGENDA = :contrasenia_agenda"
                cursor.execute(sql_query, usuario_agenda=usuario_agenda, contrasenia_agenda=contrasenia_agenda)
                columns = [col[0] for col in cursor.description]
                usuarios = [dict(zip(columns, row)) for row in cursor]

                if not usuarios:
                    raise HTTPException(status_code=404, detail="Usuario no encontrado")

                return JSONResponse(content={"usuarios_encontrados": usuarios}, status_code=200)