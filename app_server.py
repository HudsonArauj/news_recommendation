from fastapi import FastAPI, HTTPException, Query
import os
import uvicorn
from scripts.get_data import get_data
from scripts.preprocess import preprocess, process_query
from scripts.vectorizer import vectorize_text
from models.schema import QueryResponse
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carregar e processar os dados
logger.info("Carregando os dados...")
df = get_data()

# Preprocessar os textos
logger.info("Realizando preprocessamento dos textos...")
df['texto'] = df['texto'].apply(preprocess)

# Vetorização dos textos
logger.info("Vetorizando os textos...")
tfidf_matrix, vectorizer = vectorize_text(df)

# Instanciando o FastAPI
app = FastAPI()

@app.get("/query", response_model=dict)
def query_route(query: str = Query(..., description="Search query")):
    """
    Rota para processar uma query e retornar os resultados mais relevantes.
    """
    if not query:
        raise HTTPException(status_code=400, detail="Query não pode ser vazia.")
    
    logger.info(f"Processando query: {query}")
    relevant_indices, scores = process_query(query, vectorizer, tfidf_matrix)
    
    results = [
        QueryResponse(title=df.iloc[i]['titulo'], content=df.iloc[i]['texto'], relevance=scores[i])
        for i in relevant_indices[:10]
    ]

    logger.info(f"Retornando {len(results)} resultados.")
    return {"results": results, "message": "OK"}

def create_app():
    """
    Função para criar a aplicação FastAPI, permitindo sua modularização.
    """
    logger.info("Iniciando aplicação FastAPI...")
    return app

def run():
    """
    Função principal para rodar o servidor.
    """
    uvicorn.run("main:create_app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    run()
