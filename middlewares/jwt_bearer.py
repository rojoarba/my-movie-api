from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer # Importa modulo para el envio del token en las rutas
from utils.jwtmanager import validate_token # Importar funcion que creamos para generar token

#Clase para autenticar las rutas
class JWTBearer(HTTPBearer): # Se genera la clase y se hereda de HTTPBearer
    async def __call__(self, request: Request): #Función asincrona para enviar la peticion de credenciales
        auth = await super().__call__(request) # se recibe una respuesta a la petición mediante request
        data = validate_token(auth.credentials) #se valida la información del token para recibir las credenciales
        if data['email'] != "admin@gmail.com": # se verifica que el correo sea el correcto
            return HTTPException(status_code=403, detail="Credenciales incorrectas")