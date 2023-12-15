
from pydantic import BaseModel

class Usuario(BaseModel):
    ID_USUARIO: str
    NOMBRE: str
    APELLIDO_PAT: str
    APELLIDO_MAT: str = None
    USUARIO_BD: str
    CONTRASENIA_BD: str
    ENDPOINT: str
    DICCIONARIO: bytes = None
    USUARIO_AGENDA: str
    CONTRASENIA_AGENDA: str = None