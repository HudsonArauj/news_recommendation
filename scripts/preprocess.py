import re
from sklearn.metrics.pairwise import cosine_similarity

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


def process_query(query, vectorizer, tfidf_matrix):
    
    query = preprocess(query)
    
    
    query_tfidf = vectorizer.transform([query])
    
    
    cosine_similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()

    relevant_indices = cosine_similarities.argsort()[::-1]
    relevant_indices = [i for i in relevant_indices if cosine_similarities[i] > 0]
    
    return relevant_indices, cosine_similarities

