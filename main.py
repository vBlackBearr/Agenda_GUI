from fastapi import FastAPI, HTTPException
from controlador.usuario_controlador import UsuarioControlador
from modelo.usuarioBM import Usuario as usrBM
import uvicorn

app = FastAPI()
usuario_controlador = UsuarioControlador()



@app.post("/usuarios/")
def crear_usuario(usuario: usrBM):
    usuario_controlador.crear_usuario(usuario)
    return {"mensaje": "Usuario creado exitosamente"}

@app.get("/usuarios/")
def obtener_usuarios():
    return usuario_controlador.obtener_usuarios()

@app.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: str, usuario: usrBM):
    usuario.ID_USUARIO = usuario_id
    usuario_controlador.actualizar_usuario(usuario)
    return {"mensaje": "Usuario actualizado exitosamente"}

@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: str):
    usuario_controlador.eliminar_usuario(usuario_id)
    return {"mensaje": "Usuario eliminado exitosamente"}

if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=800)