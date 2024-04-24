import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import TruncatedSVD

# Define all necessary functions
def get_user_preferences():
    print("Please enter your preferred ingredients, separated by commas:")
    ingredients = input()
    print("Enter preferred tags or description:")
    tags = input()
    return ingredients, tags

def preprocess_user_input(ingredients, tags, tfidf_vectorizer):
    combined_input = ' '.join([ingredients.replace(',', ' '), tags])
    user_vector = tfidf_vectorizer.transform([combined_input])
    return user_vector

def batch_cosine_similarity(matrix, batch_size=1000):
    n = matrix.shape[0]
    similarity_matrix = np.zeros((n, n))
    for start in range(0, n, batch_size):
        end = min(start + batch_size, n)
        batch_similarity = cosine_similarity(matrix[start:end], matrix[start:end])
        similarity_matrix[start:end, start:end] = batch_similarity
    return similarity_matrix

def find_similar_recipes_from_user_input(user_vector, recipe_features_matrix, top_n=5):
    cosine_similarities = cosine_similarity(user_vector, recipe_features_matrix).flatten()
    top_indices = np.argsort(cosine_similarities)[::-1][:top_n]
    return top_indices

def display_recommendations(indices, df):
    recommended_recipes = df.iloc[indices]
    print("Recommended recipes based on your preferences:")
    print(recommended_recipes[['name', 'description']])

# Load the dataset
def load_data():
    try:
        df = pd.read_csv('dietary_tracking_app_data.csv')
        print("Data Loaded Successfully")
        return df
    except FileNotFoundError:
        print("Error: The file could not be found. Please check the file path.")
        exit()
    except Exception as e:
        print("An error occurred:", e)
        exit()

# Data preprocessing
def preprocess_data(df):
    df['tags'] = df['tags'].str.replace('[^\w\s]', '').str.lower().str.split()
    df['description'] = df['description'].astype(str).str.replace('[^\w\s]', '').str.lower().str.split()
    df['ingredients'] = df['ingredients'].str.replace('[^\w\s,]', '').str.lower().str.split(',')
    df['ingredients'] = df['ingredients'].apply(lambda x: [ingredient.strip() for ingredient in x])
    df['nutrition'] = df['nutrition'].apply(ast.literal_eval)
    return df

# Feature extraction
def feature_extraction(df):
    # Ensure all list columns are joined into single string entries
    df['tags'] = df['tags'].apply(lambda x: ' '.join(x) if isinstance(x, list) else x)
    df['description'] = df['description'].apply(lambda x: ' '.join(x) if isinstance(x, list) else x)
    df['ingredients'] = df['ingredients'].apply(lambda x: ' '.join(x) if isinstance(x, list) else x)
    
    # Concatenate the string columns
    df['combined_features'] = df['tags'] + ' ' + df['description'] + ' ' + df['ingredients']
    
    # Vectorize the combined text
    tfidf_vectorizer = TfidfVectorizer()
    recipe_features_matrix = tfidf_vectorizer.fit_transform(df['combined_features'])
    return recipe_features_matrix, tfidf_vectorizer


# Main execution functions
def main():
    df = load_data()
    df = preprocess_data(df)
    recipe_features_matrix, tfidf_vectorizer = feature_extraction(df)
    ingredients, tags = get_user_preferences()
    user_vector = preprocess_user_input(ingredients, tags, tfidf_vectorizer)
    similar_recipe_indices = find_similar_recipes_from_user_input(user_vector, recipe_features_matrix, top_n=10)
    display_recommendations(similar_recipe_indices, df)

if __name__ == "__main__":
    main()
