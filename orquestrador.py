from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="Orquestrador de Agentes")

class Pergunta(BaseModel):
    usuario: str
    pergunta: str

# URLs públicas dos agentes (variáveis de ambiente no Render)
AGENTE_MATEMATICA = os.environ.get("AGENTE_MATEMATICA_URL", "http://localhost:8001/agente_matematica")
AGENTE_BIOLOGIA = os.environ.get("AGENTE_BIOLOGIA_URL", "http://localhost:8002/agente_biologia")

@app.post("/perguntar")
def perguntar(p: Pergunta):
    # decide qual agente chamar
    texto = p.pergunta.lower()
    if "célula" in texto or "biologia" in texto:
        url = AGENTE_BIOLOGIA
    else:
        url = AGENTE_MATEMATICA

    try:
        resposta = requests.post(url, json=p.dict()).json()
        return resposta
    except Exception as e:
        return {"resposta": f"Erro ao chamar o agente: {e}"}

