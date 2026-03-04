from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel

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


class Caballero(BaseModel):
    id:int
    nombre:str
    constelacion:str
    vida:int=100
    armadura:bool=False
    cosmos:int

# Crear los caballeros del zodiaco
c1 = Caballero(id=1, nombre="Mu", constelacion="Aries", cosmos=100)
c2 = Caballero(id=2, nombre="Aldebarán", constelacion="Tauro", cosmos=95,armadura=True)
c3 = Caballero(id=3, nombre="Saga", constelacion="Géminis", cosmos=98)
c4 = Caballero(id=4, nombre="Deathmask", constelacion="Cáncer", cosmos=90)
c5 = Caballero(id=5, nombre="Aiolia", constelacion="Leo", cosmos=97)
c6 = Caballero(id=6, nombre="Shaka", constelacion="Virgo", cosmos=99)
c7 = Caballero(id=7, nombre="Dohko", constelacion="Libra", cosmos=92)
c8 = Caballero(id=8, nombre="Milo", constelacion="Escorpio", cosmos=96)
c9 = Caballero(id=9, nombre="Aiolos", constelacion="Sagitario", cosmos=100)
c10 = Caballero(id=10, nombre="Camus", constelacion="Capricornio", cosmos=94)
c11 = Caballero(id=11, nombre="Shura", constelacion="Capricornio", cosmos=93)  
c12 = Caballero(id=12, nombre="Afrodita", constelacion="Piscis", cosmos=98)

# Lista de caballeros
caballeros: list[Caballero] = [
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12
]
@app.get("/onecaballero/")
def show_one_caballero(i:int):
    return caballeros[i-1]

@app.get("/newCaballeros/") 
def show_new_caballeros(inicio:int=0, fin:int=12):
    return caballeros[inicio:fin]