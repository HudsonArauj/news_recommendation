from fastapi import FastAPI,HTTPException, Query
import os
import uvicorn
from scripts.get_data import get_data
from scripts.preprocess import preprocess,process_query
from scripts.vectorizer import vectorize_text
from models.schema import QueryResponse

df = get_data()

# preprocessamento dos textos
df['texto'] = df['texto'].apply(preprocess)

# vetorização dos textos
tfidf_matrix, vectorizer = vectorize_text(df)

app = FastAPI()

@app.get("/query")
def query_route(query: str = Query(..., description="Search query")):
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    relevant_indices, scores = process_query(query, vectorizer, tfidf_matrix)
    results = []
    for i in relevant_indices[:10]:
        results.append(QueryResponse(title=df.iloc[i]['titulo'], content=df.iloc[i]['texto'], relevance=scores[i]))
    print(len(results))    
    return {"results": results, "message": "OK"}
     

def run():
    uvicorn.run("main:app", host="0.0.0.0", port=1515)

if __name__ == "__main__":
    run()