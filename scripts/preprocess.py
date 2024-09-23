import re
import joblib

def preprocess(text):
    # Verifica se a entrada é uma string, caso contrário, retorna uma string vazia
    if not isinstance(text, str):
        return ''
    
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    # Retirar pontuação
    text = re.sub(r'[^\w\s]', '', text)
    # Retirar espaços extras
    text = re.sub(r'\s+', ' ', text)
    # Retirar espaços no início e fim
    text = text.strip()
    # Retirar stopwords
    stopwords = ['a', 'o', 'e', 'é', 'de', 'do', 'no', 'na', 'em', 'um', 'uma', 'para', 'com', 'por', 'como', 'quando', 'se', 'que', 'qual', 'quem', 'qual',
                 'mas', 'porém', 'entretanto', 'todavia', 'contudo', 'portanto', 'logo', 'assim', 'então', 'porque', 'pois']
    text = ' '.join([word for word in text.split() if word not in stopwords])
    
    return text

import os
def process_query(query):
    
    query = preprocess(query)
    
    vectorizer_path = os.path.abspath('./models/vectorizer.joblib')
    vectorizer = joblib.load(vectorizer_path)
    
    query_tfidf = vectorizer.transform([query])
    tfidf_matrix_path = os.path.abspath('./models/tfidf_matrix.joblib')
    tfidf_matrix = joblib.load(tfidf_matrix_path)
    R = tfidf_matrix.dot(query_tfidf.T)
    
    scores = R.toarray().flatten()
    
    relevant_indices = scores.argsort()[::-1]
    
    relevant_indices = [i for i in relevant_indices if scores[i] > 0]
    
    return relevant_indices, scores

