from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Agente Biologia")

class Pergunta(BaseModel):
    usuario: str
    pergunta: str

@app.post("/agente_biologia")
def responder(p: Pergunta):
    # respostas simples de exemplo
    if "célula" in p.pergunta.lower():
        resposta = "A célula é a unidade básica da vida."
    else:
        resposta = "Não sei responder essa pergunta de biologia."
    return {"resposta": resposta}

