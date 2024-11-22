import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load a sample text dataset (assuming text column is present in 'Comments' column)
data = pd.read_csv('powerconsumption.csv')

if 'Comments' in data.columns:
    # Vectorize the text data
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data['Comments'].dropna())

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    data['Cluster'] = kmeans.fit_predict(X)

    print("\nDocument Clustering Results (First 10 Rows):")
    print(data[['Comments', 'Cluster']].head(10))
else:
    print("No 'Comments' column found for text-based document clustering.")
