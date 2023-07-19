from jwt import encode, decode # Se importa desde la libreria jwt el modulo encode para generar el token

# Función que devuelve un token generado con jwt
def create_token(data: dict) -> str: 
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token
# Función que decodifica el token para validarlo
def validate_token(token: str) -> dict:
    data = decode(token, key="my_secret_key", algorithms=['HS256'])
    return data





