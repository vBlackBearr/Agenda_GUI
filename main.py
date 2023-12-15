from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from controlador.usuario_controlador import UsuarioControlador

app = FastAPI()
usuario_controlador = UsuarioControlador()

class Usuario(BaseModel):
    id: str
    nombre: str
    correo: str

@app.post("/usuarios/")
def crear_usuario(usuario: Usuario):
    usuario_controlador.crear_usuario(usuario)
    return {"mensaje": "Usuario creado exitosamente"}

@app.get("/usuarios/")
def obtener_usuarios():
    return usuario_controlador.obtener_usuarios()

@app.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: str, usuario: Usuario):
    usuario.id = usuario_id
    usuario_controlador.actualizar_usuario(usuario)
    return {"mensaje": "Usuario actualizado exitosamente"}

@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: str):
    usuario_controlador.eliminar_usuario(usuario_id)
    return {"mensaje": "Usuario eliminado exitosamente"}