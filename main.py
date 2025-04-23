from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola desde tu backend!"}

@app.get("/suma")
def sumar(a: int, b: int):
    return {"resultado": a + b}
