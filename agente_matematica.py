from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Agente Matemática")

class Pergunta(BaseModel):
    usuario: str
    pergunta: str

@app.post("/agente_matematica")
def responder(p: Pergunta):
    # respostas simples de exemplo
    if "derivada" in p.pergunta.lower():
        resposta = "A derivada de x² é 2x."
    else:
        resposta = "Não sei responder essa pergunta de matemática."
    return {"resposta": resposta}

