from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_text(df):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['texto'])
    return tfidf_matrix, vectorizer
