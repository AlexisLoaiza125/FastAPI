from fastapi import FastAPI
from datetime import date

app = FastAPI()

@app.get("/holalalallala")
def hello():
    return {"hello":"in FastAPI"}

@app.get("/sumar/{a}/{b}")
def sumar(a,b):
    res = int(a) + int(b)    
    return {"resultado":res}

@app.get("/concat/{a}/{b}")
def concat(a,b):
    res = a + b    
    return {"resultado":res}

#construir un endpoint que reciba nombre y fecha de nacimiento debe retornar el nombre y la edad.
@app.get("/edad")
def calcular_edad(nombre: str, fecha_nacimiento_AAAAMMDD: date):
    hoy = date.today()
    
    edad = hoy.year - fecha_nacimiento_AAAAMMDD.year
    if (hoy.month, hoy.day) < (fecha_nacimiento_AAAAMMDD.month, fecha_nacimiento_AAAAMMDD.day):
        edad -= 1

    return {
        "nombre": nombre, 
        "edad (AAAA/MM/DD)": edad
    }
#orden.
@app.get("/user/me")
def read_me_user():
    return {"user_id":"users logeado"}

@app.get("/user/{id}")
def read_user(id: str):
    return {"user_id": id}


@app.get("/users")
def show_users():
    return ["1", "2", "3", "4", "5"]
